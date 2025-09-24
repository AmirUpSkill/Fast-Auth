import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


class UserService:
    """
        Service layer for all user-related business logic 
    """
    def get_user_by_email(self,db:Session,*,email:str) -> User | None:
        """
        Retrieves a user by their email address.

        Args:
            db: The database session.
            email: The email of the user to retrieve.

        Returns:
            The User object if found, otherwise None.
        """
        return db.query(User).filter(User.email == email).first()
    def get_user_by_id(self, db: Session, *, user_id: uuid.UUID) -> User | None:
        """
        Retrieves a user by their unique ID.

        Args:
            db: The database session.
            user_id: The ID of the user to retrieve.

        Returns:
            The User object if found, otherwise None.
        """
        return db.query(User).filter(User.id == user_id).first()
    def create_user(self, db: Session, *, user_in: UserCreate) -> User:
        """
        Creates a new user in the database.

        Args:
            db: The database session.
            user_in: The Pydantic schema with the user's creation data.

        Returns:
            The newly created User object.
        """
        # --- Create a new User Model ---
        db_user = User(
            name=user_in.name,
            email=user_in.email,
            avatar_url=user_in.avatar_url,
            created_at=datetime.now(timezone.utc)
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    def get_or_create(self, db: Session, *, user_in: UserCreate) -> User:
        """
        Retrieves a user by email, or creates a new one if they don't exist.
        This is the primary method used during the OAuth callback flow.

        Args:
            db: The database session.
            user_in: The Pydantic schema with user data from the OAuth provider.

        Returns:
            An existing or newly created User object.
        """
        # --- Check if user Exists --- 
        user = self.get_user_by_email(db, email=user_in.email)
        if user:
            return user 
        return self.create_user(db,user_in=user_in)
# --- Create Instance --- 
user_service = UserService()