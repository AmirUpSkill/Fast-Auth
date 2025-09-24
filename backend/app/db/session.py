from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# --- Create the SQLAlchemy engine ---
engine = create_engine(settings.DB_URL, pool_pre_ping=True)
# --- Create Local Session ---
SessionLocal = sessionmaker(autocommit=False , autoflush=False)
# --- Get DB --- 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()