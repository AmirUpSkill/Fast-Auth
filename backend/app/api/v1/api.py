from fastapi import APIRouter
from app.api.v1.endpoints import auth, users

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/api/v1/users", tags=["users"])
