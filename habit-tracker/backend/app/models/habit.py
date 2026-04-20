from datetime import datetime, timezone, date
from pydantic import Field, model_validator
from beanie import Document

from pymongo import ASCENDING, IndexModel

class Habit(Document):
    name: str = Field(min_length=1)
    owner_id: int
    status: str
    
    remind_time: str 
    start_date: date
    end_date: date
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @model_validator(mode="after")
    def validate_dates(self):
        
        if self.end_date < self.start_date:
            raise ValueError("end date should not be before start date")
        
        if self.start_date < date.today():
            raise ValueError("start date should not be in the past")
            
        return self

    class Settings:
        name = "habits"

        indexes = [
            IndexModel(
                [("name", ASCENDING), ("owner_id", ASCENDING)],
                unique=True,
                name="unique_habit_name_per_user"
            )
        ]
