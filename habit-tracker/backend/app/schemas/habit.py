from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class HabitBase(BaseModel):
    habit_name: str = Field(min_length = 3, max_length = 50)
    habit_status: str
    owner_id: int
    
    start_date: datetime
    end_date: datetime

class HabitCreate(BaseModel):
    pass

class HabitOut(HabitBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes = True, populate_by_name = True)

class HabitUpdate(BaseModel):
    habit_name: Optional[str] = Field(default = None, min_lenght = 3, max_length = 50)
    habit_status: Optional[str] = Field(default = None)
    
    star_date: Optional[datetime] = Field(default = None)
    end_date: Optional[datetime] = Field(default = None)