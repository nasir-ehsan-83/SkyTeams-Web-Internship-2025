from beanie import Document
from datetime import datetime

class User(Document):
    email: str
    hashed_password: str
    is_active: bool = True
    created_at: datetime = datetime.utcnow()

    class Settings:
        name = "users"