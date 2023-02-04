import uuid
from typing import Dict

from fastapi import APIRouter, HTTPException, status

from common.authentication import (
    authenticate_user,
    create_access_token,
    get_password_hash,
)
from models import User
from schemas.users_schema import (
    UserRequestLoginSchema,
    UserRequestSchema,
    UserResponseSchema,
)

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create", response_model=UserResponseSchema)
async def create_user(user: UserRequestSchema) -> User:
    """Create User."""
    user_check = await User.find_one(User.email == user.email)
    if user_check:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email already exists"
        )
    user_data = user.dict()
    user_data["uuid"] = str(uuid.uuid4())
    user_data["password"] = get_password_hash(user.password)
    return await User(**user_data).create()


@router.post("/login")
async def login_user(user: UserRequestLoginSchema) -> Dict:
    """Login_user will allow user to login if the provided creds are
    correct."""
    user_data = await authenticate_user(email=user.email, password=user.password)
    if not user_data:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = create_access_token(
        data={
            "id": user_data.uuid,
            "email": user_data.email,
        }
    )
    return {"status": "success", "access_token": access_token, "token_type": "bearer"}
