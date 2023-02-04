from pydantic import BaseModel, EmailStr


class UserRequestSchema(BaseModel):
    first_name: str
    last_name: str
    password: str
    email: EmailStr


class UserResponseSchema(BaseModel):
    uuid: str
    first_name: str
    last_name: str
    email: EmailStr


class UserRequestLoginSchema(BaseModel):
    email: EmailStr
    password: str
