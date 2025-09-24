from fastapi import APIRouter, Depends
from app.schemas.user import User as UserSchema
from app.security.deps import CurrentUser

router = APIRouter()

@router.get("/me", response_model=UserSchema)
async def read_users_me(current_user: CurrentUser):
    return current_user