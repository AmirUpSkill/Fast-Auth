from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
import uuid

class UserBase(BaseModel):
    email: EmailStr
    name: str
    avatar_url: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    avatar_url: Optional[str] = None

class UserInDB(UserBase):
    id: uuid.UUID
    created_at: datetime
    
    class Config:
        from_attributes = True

class UserResponse(UserInDB):
    """Schema for returning a user from the API"""
    pass