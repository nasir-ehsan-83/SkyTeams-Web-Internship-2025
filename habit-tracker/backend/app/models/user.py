from typing import Annotated 
from beanie import Document, Indexed
from datetime import datetime
from pydantic import EmailStr, Field

class User(Document):
    name: str
    username: str
    email: Annotated[EmailStr, Indexed(unique=True)]
    password: str
    is_active: bool = True
    created_at: datetime = Field(default_factory = datetime.utcnow)
    updated_at: datetime = Field(default_factory = datetime.utcnow)

    class Settings:
        name = "users"
