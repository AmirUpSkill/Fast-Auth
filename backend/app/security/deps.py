from typing import Annotated
from fastapi import Depends, HTTPException, status, Request
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_db
from app.models.user import User  
from app.schemas.user import UserResponse 
from app.services.user_service import user_service

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

def get_current_user(  
    request: Request, 
    db: Annotated[Session, Depends(get_db)]
) -> User:
    """
    Dependency to get the current authenticated user.
    Reads token from HttpOnly cookie, validates it, and fetches user from DB.
    """
    token = request.cookies.get("access_token")
    
    if token is None:
        raise credentials_exception
    
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        email: str | None = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = user_service.get_by_email(db, email=email)
    
    if user is None:
        raise credentials_exception
    
    return user

CurrentUser = Annotated[User, Depends(get_current_user)]