import uuid 
from datetime import datetime 
from pydantic import BaseModel 

# --- Base Schema --- 
class UserBase(BaseModel):
    """
        Base Schema for a User 
    """
    email: str 
    name: str 
    avatar_url: str | None = None 

class UserCreate(UserBase):
    pass 

# --- Read/Response Schema --- 
class User(UserBase):
    """
        Schema for returning a user form the API 
    """
    id: uuid.UUID
    created_at: datetime 
    # --- Config --- 
    model_config = ConfigDict(
        from_attributes=True,
    )