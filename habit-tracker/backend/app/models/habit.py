from datetime import datetime, timezone
from pydantic import Field
from pymongo import IndexModel, ASCENDING
from beanie import Document

class Habit(Document):
    name: str
    status: str
    start_date: datetime
    end_date: datetime

    # Use default_factory so the time is captured at the moment of creation
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "habits"

        indexes = [
            IndexModel(["name", str(ASCENDING)], unique = True)
        ]