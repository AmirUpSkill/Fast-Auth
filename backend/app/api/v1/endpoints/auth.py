import secrets
from fastapi import APIRouter, Request, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from urllib.parse import urlencode
from app.db.session import get_db
from app.core.config import settings
from app.services.auth_service import auth_service

router = APIRouter()

# --- Helper: Generate CSRF state ---
def generate_state() -> str:
    return secrets.token_urlsafe(32)

# --- Endpoint 1: Initiate Google OAuth Login ---
@router.get("/google/login")
async def google_login(request: Request):
    state = generate_state()
    # Store state in session cookie (for CSRF protection)
    response = RedirectResponse(url="/")
    response.set_cookie(
        key="oauth_state",
        value=state,
        httponly=True,
        max_age=600,  # 10 minutes
        secure=not settings.FRONTEND_URL.startswith("http://localhost"),
        samesite="lax"
    )

    params = {
        "response_type": "code",
        "client_id": settings.GOOGLE_CLIENT_ID,
        "redirect_uri": f"{settings.FRONTEND_URL}/api/v1/auth/google/callback",
        "scope": "openid email profile",
        "state": state,
        "access_type": "offline",
        "prompt": "select_account"
    }
    google_auth_url = f"https://accounts.google.com/o/oauth2/v2/auth?{urlencode(params)}"
    return RedirectResponse(url=google_auth_url)

# --- Endpoint 2: Google OAuth Callback ---
@router.get("/google/callback")
async def google_callback(
    request: Request,
    code: str,
    state: str,
    db: Session = Depends(get_db)
):
    # 1. Validate state (CSRF)
    stored_state = request.cookies.get("oauth_state")
    if not stored_state or stored_state != state:
        raise HTTPException(status_code=400, detail="Invalid state parameter")

    try:
        # 2. Authenticate user & get JWT
        jwt_token = await auth_service.authenticate_google_user(code=code, db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    # 3. Redirect to frontend home + set auth cookie
    response = RedirectResponse(url="/")
    response.set_cookie(
        key="access_token",
        value=jwt_token,
        httponly=True,
        max_age=60 * settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        secure=not settings.FRONTEND_URL.startswith("http://localhost"),
        samesite="lax"
    )
    # Clear the oauth_state cookie
    response.delete_cookie("oauth_state")
    return response

# --- Endpoint 3: Logout ---
@router.post("/logout")
async def logout():
    response = RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    response.delete_cookie("access_token")
    return response