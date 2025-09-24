from fastapi import APIRouter, Depends
from app.models.user import User
from app.schemas.user import User as UserSchema
from app.security.deps import get_current_user

router = APIRouter()

@router.get("/me", response_model=UserSchema)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user