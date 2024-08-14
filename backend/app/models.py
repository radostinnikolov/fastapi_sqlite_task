from sqlalchemy import Column, String, Integer, Float
from app.database import BASE


class Order(BASE):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    sender_name = Column(String)
    receiver_name = Column(String)
    sender_email = Column(String)
    sender_phone = Column(String)
    receiver_phone = Column(String)
    item = Column(String)
    quantity = Column(Integer)
    weight = Column(Float)
