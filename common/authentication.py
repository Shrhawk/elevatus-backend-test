from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JOSEError, jwt
from passlib.context import CryptContext

from config.config import settings
from models import Candidate, User

security = HTTPBearer()
PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return PWD_CONTEXT.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return PWD_CONTEXT.hash(password)


async def authenticate_user(email: str, password: str) -> User:
    """Authenticate user for login."""
    user = await User.find_one(Candidate.email == email)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


def create_access_token(data: dict) -> str:
    return _create_token(
        token_type="access_token",
        lifetime=timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES)),
        payload=data,
    )


def _create_token(
    token_type: str,
    lifetime: timedelta,
    payload: dict,
) -> str:
    """_create_token will create a jwt token."""
    expire = datetime.utcnow() + lifetime
    payload["type"] = token_type
    payload["exp"] = expire
    payload["iat"] = datetime.utcnow()
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> User:
    """get_current_user will validate jwt token from request also will return
    the current logged-in user object."""
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={"verify_aud": False},
        )
        email: str = payload.get("email")
    except JOSEError:
        raise credentials_exception
    user = await User.find_one(Candidate.email == email)
    if user is None:
        raise credentials_exception
    return user
