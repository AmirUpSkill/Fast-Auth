from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.api import api_router

# --- Initialize FastAPI App ---
app = FastAPI(
    title="Fast Auth",
    description="A minimal, secure Google OAuth template for FastAPI + Next.js",
    version="1.0.0",
    docs_url="/api/docs",        
    redoc_url="/api/redoc",      
    openapi_url="/api/openapi.json"
)

# --- CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Include API Routes ---
app.include_router(api_router)