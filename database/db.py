from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config.config import settings
from models import Candidate, User


async def initiate_database():
    client = AsyncIOMotorClient(settings.DATABASE_URL)
    await init_beanie(
        database=client.get_default_database(), document_models=[User, Candidate]
    )
