from typing import Dict

from fastapi import Depends, FastAPI

from common.authentication import get_current_user
from database.db import initiate_database
from routes.candidate import router as candidate_router
from routes.user import router as user_router

app = FastAPI()


@app.on_event("startup")
async def start_database():
    await initiate_database()


@app.get("/ping", tags=["Health"])
async def read_root() -> Dict:
    return {"message": "pong"}


PROTECTED = [Depends(get_current_user)]

app.include_router(user_router)
app.include_router(candidate_router, dependencies=PROTECTED)
