import httpx

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from app import models, auth
from app.schemas import OrderSchema, UserSchema, Token, User
from app.database import ENGINE, access_db

from sqlalchemy.orm import Session
from typing_extensions import Annotated
from datetime import timedelta

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.BASE.metadata.create_all(ENGINE)
password_context = auth.get_context()



@app.post("/create-order")
async def create_order(order_request: OrderSchema, current_user: Annotated[User, Depends(auth.get_current_user)], db: Session = Depends(access_db)):
    try:
        new_order = models.Order(**dict(order_request))
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        return order_request
    except Exception as e:
        raise e
    finally:
        async with httpx.AsyncClient() as client:
            response = await client.post("http://172.19.0.4:8001/save-user-info", json={
            "sender_name": order_request.sender_name,
            "sender_email": order_request.sender_email,
            "sender_phone": order_request.sender_phone
        }, headers={
                "Content-Type": "application/json"
            })
            print(response.json())



@app.get("/orders")
def get_all_orders(current_user: Annotated[User, Depends(auth.get_current_user)], db: Session = Depends(access_db)):
    orders = db.query(models.Order).all()
    return orders


@app.delete("/orders/{order_id}")
async def delete_order(order_id, current_user: Annotated[User, Depends(auth.get_current_user)], db: Session = Depends(access_db)):
    try:
        db.query(models.Order).filter(models.Order.id == order_id).delete(synchronize_session=False)
        db.commit()
        return {"item is deleted"}
    except Exception as e:
        raise e
    finally:
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"http://172.19.0.4:8001/remove/{order_id}")
            print(response.json())


@app.post("/sign-up")
async def create_user(request: UserSchema, db: Session = Depends(access_db)):
    hashed_password = password_context.hash(request.password)
    new_user = models.User(
        username=request.username,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {f"user {request.username} is created"}

@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(access_db)
) -> Token:
    user = auth.authenticate_user(pwd_context=password_context, username=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
