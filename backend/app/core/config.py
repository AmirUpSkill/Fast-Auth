from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # --- DB Configuration ---
    DB_URL: str = Field(..., description="Database connection URL")
    
    # --- Google OAuth Configuration ---
    GOOGLE_CLIENT_ID: str = Field(..., description="Google OAuth client ID")
    GOOGLE_CLIENT_SECRET: str = Field(..., description="Google OAuth client secret")
    
    # --- URL For Redirection ---
    FRONTEND_URL: str = Field(..., description="Frontend application URL")
    BACKEND_URL: str = Field(..., description="Backend application URL")
    
    # --- Secret Management Configuration ---
    SECRET_KEY: str = Field(..., description="Secret key for JWT signing")
    ALGORITHM: str = Field(default="HS256", description="JWT algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, description="Access token expiration time in minutes")

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": True,
        "extra": "ignore"
    }


settings = Settings()