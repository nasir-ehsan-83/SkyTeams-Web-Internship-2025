from datetime import datetime
from pydantic import EmailStr, Field
from pymongo import IndexModel, ASCENDING
from beanie import Document

class User(Document):
    name: str
    username: str
    email: EmailStr  
    password: str
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "users"
        # Correct way to define unique indexes in Beanie Settings
        indexes = [
            IndexModel([("email", ASCENDING)], unique=True),
            IndexModel([("username", ASCENDING)], unique=True),
        ]
