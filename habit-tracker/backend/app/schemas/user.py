from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, Field
from datetime import datetime

class UserBase(BaseModel):
    username: str = Field(min_length = 3, max_length = 30)
    email: EmailStr

class UserCreate(BaseModel):
    password: str = Field(min_length = 8)

class UserResponse(BaseModel):
    id: Optional[str] = Field(alias = "_id")
    created_at: datetime
    is_active: bool

    model_config = ConfigDict(from_attributes = True, populate_by_name = True)

class UserUpdate(BaseModel):
    username: Optional[str] = Field(min_length = 3, max_length = 30)
    email: Optional[EmailStr]
    password: Optional[str] = Field(min_length = 8)