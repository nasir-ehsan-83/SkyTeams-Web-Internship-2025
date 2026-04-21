from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, Field, field_validator
from datetime import datetime
from bson import ObjectId 

class UserBase(BaseModel):
    name: str = Field(min_length = 3, max_length = 50)
    username: str = Field(min_length = 3, max_length = 30)
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(min_length = 8)

class UserOut(UserBase):
    id: Optional[str] = Field(alias="_id")
    created_at: datetime
    updated_at: datetime
    is_active: bool

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    @field_validator("id", mode="before")
    @classmethod
    def convert_objectid(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return 

class UserUpdateBase(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None

class UserUpdate(BaseModel):
    email: EmailStr
    update_data: UserUpdateBase