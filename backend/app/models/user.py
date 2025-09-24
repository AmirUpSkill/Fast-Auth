import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base

class User(Base):
    """
        Database model for a user . 
    """
    __tablename__ = "users"
    # --- Table Attributes --- 
    id: uuid.UUID = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    name: str = Column(
        String,
        nullable=False 
    )
    email: str = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )
    avatar_url: str | None = Column(
        String,
        nullable=True 
    )
    created_at: datetime = Column(
        DateTime,
        nullable=False
    )