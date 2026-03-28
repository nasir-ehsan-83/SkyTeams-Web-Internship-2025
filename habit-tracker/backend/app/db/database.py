from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.core.confing import settings
from app.models.user import User

async def init_db():
    client = AsyncIOMotorClient( f'mongodb://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}')

    await init_beanie(
        database = client[settings.database_name],
        document_models = [User]
    )