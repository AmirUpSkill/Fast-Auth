from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings

app = FastAPI(title="Fast Auth API", openapi_url="/api/v1/openapi.json")

@app.get("/")
async def root():
    return {"message": "Fast Auth is running!"}

app.include_router(api_router)