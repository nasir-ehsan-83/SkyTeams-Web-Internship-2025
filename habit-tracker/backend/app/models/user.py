from typing import Annotated 
from beanie import Document, Indexed
from datetime import datetime
from pydantic import EmailStr, Field

class User(Document):
    email: Annotated[EmailStr, Indexed(unique=True)]
    username: str
    hashed_password: str
    is_active: bool = True
    created_at: datetime = Field(default_factory = datetime.utcnow)

    class Settings:
        name = "users"
