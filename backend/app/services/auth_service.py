import httpx
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.config import settings
from app.schemas.user import UserCreate
from app.services.user_service import user_service
from app.security.core import create_access_token

class AuthService:
    """
        Auth Service with the goal to 
            - 1 : Fetching Google's access token using the OAuth code 
            - 2 : Retrieving user profile info from Google's userinfo endpoint 
            - 3 : Using user_service.get_or_create()  to persist or fetch the user 
            - 4 : Generating a JWT session token 
    """
    GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
    GOOGLE_USERINFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"

    async def authenticate_google_user(self, code: str, db: Session) -> str:
        """
        Authenticates a user via Google OAuth code.
        Returns a JWT access token if successful.
        """
        # --- Step 1: Exchange code for access token ---
        token_data = await self._exchange_code_for_token(code)
        access_token = token_data.get("access_token")
        if not access_token:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to retrieve access token from Google"
            )
        # --- Step 2 : Fetch user info from Google --- 
        user_info = await self._fetch_user_info(access_token)
        email = user_info.get("email")
        name = user_info.get("name")
        picture = user_info.get("picture")
        if not email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Google did not return an email address."
            )
        if not user_info.get("email_verified", False):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Google account email is not verified."
            )
        # --- Step 3 : Upsert user in DB --- 
        user_in = UserCreate(
            email=email,
            name=name or email.split("@")[0],
            avatar_url=picture 
        )
        user = user_service.get_or_create(db=db, user_in=user_in)
        # --- Step 4 : Create JWT session token ---
        jwt_token = create_access_token(data={"sub": user.email})
        return jwt_token
    
    async def _exchange_code_for_token(self, code: str) -> dict:
        """Exchanges OAuth code for access token."""
        redirect_uri = f"{settings.BACKEND_URL}/api/v1/auth/google/callback"
        
    
        print(f"DEBUG: AuthService token exchange redirect_uri: {redirect_uri}")
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.GOOGLE_TOKEN_URL,
                data={
                    "client_id": settings.GOOGLE_CLIENT_ID,
                    "client_secret": settings.GOOGLE_CLIENT_SECRET,
                    "code": code,
                    "grant_type": "authorization_code",
                    "redirect_uri": redirect_uri,  
                },
                headers={"Accept": "application/json"},
            )
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Google token exchange failed: {response.text}"
            )
        return response.json()

    async def _fetch_user_info(self, access_token: str) -> dict:
        """Fetches user profile from Google."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                self.GOOGLE_USERINFO_URL,
                headers={"Authorization": f"Bearer {access_token}"},
            )
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to fetch user info from Google."
            )
        return response.json()


#  ---  Singleton instance ---- 
auth_service = AuthService()