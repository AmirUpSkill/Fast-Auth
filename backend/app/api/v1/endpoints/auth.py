import secrets
from fastapi import APIRouter, Request, Response, Depends, status, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from urllib.parse import urlencode

from app.db.session import get_db
from app.core.config import settings
from app.services.auth_service import auth_service
from app.security.deps import CurrentUser
from app.schemas.user import User as UserSchema

router = APIRouter()

# --- Step 1: Initiate Google Login ---
@router.get("/google/login")
async def google_login(request: Request):
    state = secrets.token_urlsafe(32)
    response = RedirectResponse(url="https://accounts.google.com/o/oauth2/v2/auth")
    response.set_cookie(
        key="oauth_state",
        value=state,
        httponly=True,
        max_age=600,  # 10 minutes
        secure=True if settings.FRONTEND_URL.startswith("https") else False,
        samesite="lax"
    )
    params = {
        "response_type": "code",
        "client_id": settings.GOOGLE_CLIENT_ID,
        "redirect_uri": f"{settings.FRONTEND_URL}/api/v1/auth/google/callback",
        "scope": "openid email profile",
        "state": state,
        "access_type": "offline",
    }
    response.headers["Location"] += "?" + urlencode(params)
    return response


# --- Step 2: Google OAuth Callback ---
@router.get("/google/callback")
async def google_callback(
    request: Request,
    code: str,
    state: str,
    db: Session = Depends(get_db)
):
    # Validate state (CSRF protection)
    stored_state = request.cookies.get("oauth_state")
    if not stored_state or stored_state != state:
        raise HTTPException(status_code=400, detail="Invalid state parameter")

    # Authenticate user and get JWT
    jwt_token = await auth_service.authenticate_google_user(code=code, db=db)

    # Redirect to frontend home
    response = RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    response.set_cookie(
        key="access_token",
        value=jwt_token,
        httponly=True,
        secure=True if settings.FRONTEND_URL.startswith("https") else False,
        samesite="lax",
        max_age=60 * settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    # Clear the oauth_state cookie
    response.delete_cookie("oauth_state")
    return response


# --- Step 3: Logout ---
@router.post("/logout")
async def logout(current_user: CurrentUser):
    response = Response(status_code=status.HTTP_200_OK)
    response.set_cookie(
        key="access_token",
        value="",
        expires=0,
        max_age=0,
        httponly=True,
        secure=True if settings.FRONTEND_URL.startswith("https") else False,
        samesite="lax"
    )
    return {"message": "Successfully logged out"}