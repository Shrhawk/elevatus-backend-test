from pydantic import EmailStr

from models.base_model import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    uuid: str
    password: str
