import secrets
from fastapi import APIRouter, Request, Depends, HTTPException, status
from fastapi.responses import RedirectResponse, JSONResponse
from sqlalchemy.orm import Session
from urllib.parse import urlencode

from app.db.session import get_db
from app.core.config import settings
from app.services.auth_service import auth_service

router = APIRouter()

def generate_state() -> str:
    return secrets.token_urlsafe(32)

@router.get("/google/login")
async def google_login(request: Request):
    """Initiate Google OAuth2 authentication flow"""
    state = generate_state()
    redirect_uri = f"{settings.BACKEND_URL}/api/v1/auth/google/callback"
    
    print(f"DEBUG: Authorization redirect_uri: {redirect_uri}")
    
    params = {
        "response_type": "code",
        "client_id": settings.GOOGLE_CLIENT_ID,
        "redirect_uri": redirect_uri,
        "scope": "openid email profile",
        "state": state,
        "access_type": "offline",
        "prompt": "select_account"
    }
    
    google_auth_url = f"https://accounts.google.com/o/oauth2/v2/auth?{urlencode(params)}"
    
    response = RedirectResponse(url=google_auth_url)
    response.set_cookie(
        key="oauth_state",
        value=state,
        httponly=True,
        max_age=600,
        secure=False,  
        samesite="lax"
    )
    return response

@router.get("/google/callback")
async def google_callback(
    request: Request,
    code: str,
    state: str,
    db: Session = Depends(get_db)
):
    """Handle the callback from Google after user consent"""
    stored_state = request.cookies.get("oauth_state")
    if not stored_state or stored_state != state:
        raise HTTPException(
            status_code=400, 
            detail="Invalid state parameter - possible CSRF attack"
        )

    try:
        jwt_token = await auth_service.authenticate_google_user(code=code, db=db)
    except HTTPException:
        raise
    except Exception as e:
        print(f"ERROR: Authentication failed: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Authentication failed: {str(e)}"
        )

    # Redirect to frontend dashboard with secure cookie
    response = RedirectResponse(url=f"{settings.FRONTEND_URL}/dashboard")
    response.set_cookie(
        key="access_token",
        value=jwt_token,
        httponly=True,
        max_age=60 * settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        secure=False,  
        samesite="lax",
        domain="localhost",  
        path="/" 
    )
    
    # ---  Clean up CSRF cookie ---
    response.delete_cookie("oauth_state")
    return response

@router.post("/logout")
async def logout():
    """Log out user by clearing their session cookie"""
    response = JSONResponse(content={"message": "Successfully logged out"})
    response.delete_cookie(
        key="access_token",
        httponly=True,
        samesite="lax",
        domain="localhost",
        path="/"
    )
    return response