from sqlalchemy import Column, String, Integer
from app.database import BASE


class UserInfo(BASE):
    __tablename__ = "user_info"
    id = Column(Integer, primary_key=True, index=True)
    sender_name = Column(String)
    sender_email = Column(String)
    sender_phone = Column(String)

