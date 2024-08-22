from fastapi import FastAPI
from fastapi.params import Depends
from app import models
from app.schemas import UserInfoSchema
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


@app.post("/save-user-info")
def user_info(request: UserInfoSchema, db: Session = Depends(access_db)):
    new_order = models.UserInfo(**dict(request))
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return request

@app.delete("/remove/{entry_id}")
def delete_entry(entry_id, db: Session = Depends(access_db)):
    db.query(models.UserInfo).filter(models.UserInfo.id == entry_id).delete(synchronize_session=False)
    db.commit()
    return {"item from backend service 2 is deleted"}

