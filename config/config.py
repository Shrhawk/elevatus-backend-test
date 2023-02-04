from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    ACCESS_TOKEN_EXPIRE_MINUTES: Optional[str] = None
    JWT_SECRET: Optional[str] = None
    ALGORITHM: Optional[str] = None

    class Config:
        env_file = ".env"
        orm_mode = True


settings = Settings()
