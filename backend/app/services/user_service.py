from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

class UserService:
    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        """Get user by email"""
        return db.query(User).filter(User.email == email).first()
    
    def get_or_create(self, db: Session, user_in: UserCreate) -> User:
        """Get existing user or create new one"""
        user = self.get_by_email(db=db, email=user_in.email)
        
        if user:
            db.query(User).filter(User.email == user_in.email).update({
                "name": user_in.name,
                "avatar_url": user_in.avatar_url
            })
            db.commit()
            db.refresh(user)
            return user
        else:
            # ---   Create new user  ---- 
            user = User(
                email=user_in.email,
                name=user_in.name,
                avatar_url=user_in.avatar_url
            )
            db.add(user)
            db.commit()
            db.refresh(user)
            return user

user_service = UserService()