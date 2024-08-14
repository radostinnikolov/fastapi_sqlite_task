from pydantic import BaseModel


class OrderSchema(BaseModel):
    sender_name: str
    receiver_name: str
    sender_email: str
    sender_phone: str
    receiver_phone: str
    item: str
    quantity: int
    weight: float

