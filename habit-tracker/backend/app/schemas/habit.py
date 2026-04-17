from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class HabitBase(BaseModel):
    name: str = Field(min_length = 3, max_length = 50)
    status: str
    
    start_date: datetime
    end_date: datetime

class HabitCreate(HabitBase):
    pass

class HabitOut(HabitBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes = True, populate_by_name = True)

class HabitUpdate(BaseModel):
    name: Optional[str] = Field(default = None, min_lenght = 3, max_length = 50)
    status: Optional[str] = Field(default = None)
    
    star_date: Optional[datetime] = Field(default = None)
    end_date: Optional[datetime] = Field(default = None)