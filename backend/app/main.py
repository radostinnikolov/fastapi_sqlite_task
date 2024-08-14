from fastapi import FastAPI
from fastapi.params import Depends
from app import models
from app.schemas import OrderSchema
from app.database import ENGINE, access_db
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

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


@app.post("/create-order")
def create_order(order_request: OrderSchema, db: Session = Depends(access_db)):
    new_order = models.Order(**dict(order_request))
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return order_request


@app.get("/orders")
def get_all_orders(db: Session = Depends(access_db)):
    orders = db.query(models.Order).all()
    return orders


@app.delete("/orders/{order_id}")
def delete_order(order_id, db: Session = Depends(access_db)):
    db.query(models.Order).filter(models.Order.id == order_id).delete(synchronize_session=False)
    db.commit()
    return {"item is deleted"}