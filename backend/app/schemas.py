from pydantic import BaseModel
from typing import Union


class OrderSchema(BaseModel):
    sender_name: str
    receiver_name: str
    sender_email: str
    sender_phone: str
    receiver_phone: str
    item: str
    quantity: int
    weight: float

class UserSchema(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    username: str


