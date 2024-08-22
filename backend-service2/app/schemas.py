from pydantic import BaseModel


class UserInfoSchema(BaseModel):
    sender_name: str
    sender_email: str
    sender_phone: str


