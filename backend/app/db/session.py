from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# ---  Create database engine ----
engine = create_engine(
    settings.DB_URL,
    echo=False,  
    pool_pre_ping=True,  
)

# ---   Create SessionLocal class ---- 
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

def get_db():
    """Database dependency for FastAPI"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()