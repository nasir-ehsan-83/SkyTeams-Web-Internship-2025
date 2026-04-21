from datetime import datetime, timezone
from pydantic import EmailStr, Field
from pymongo import IndexModel, ASCENDING
from beanie import Document

class User(Document):
    name: str
    username: str
    email: EmailStr  
    password: str
    is_active: bool = True
    
    created_at: datetime = Field(default_factory = lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory = lambda: datetime.now(timezone.utc))

    class Settings:
        name = "users"
        # Correct way to define unique indexes in Beanie Settings
        indexes = [
            IndexModel([("email", ASCENDING)], unique=True),
            IndexModel([("username", ASCENDING)], unique=True),
        ]
