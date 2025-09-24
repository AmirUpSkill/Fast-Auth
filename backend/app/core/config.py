from pydantic_settings import BaseSettings 
from pydantic import Field               

class Settings(BaseSettings):
    # --- DB Configuration ---
    DB_URL: str = Field(..., env="DB_URL")
    
    # --- Google Oauth Configuration 
    GOOGLE_CLIENT_ID: str = Field(..., env="GOOGLE_CLIENT_ID")
    
    GOOGLE_CLIENT_SECRET: str = Field(..., env="GOOGLE_CLIENT_SECRET")
    
    # --- Secret Management Configuration  ---
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    
    ALGORITHM: str = Field("HS256", env="ALGORITHM")
    
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(30, env="ACCESS_TOKEN_EXPIRE_MINUTES")

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()