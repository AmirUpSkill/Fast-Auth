import pytest
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

from app.db.session import engine 

def test_database_connection():
    """
    GIVEN a database URL configured in the environment
    WHEN the engine tries to connect and execute a simple query
    THEN it should succeed without raising an exception
    """
    try:
       
        with engine.connect() as connection:
            
            result = connection.execute(text("SELECT 1"))
            
            
            row = result.scalar()
            
            
            assert row == 1
            
    except OperationalError as e:
        # If an OperationalError occurs, the test fails.
        # This is useful for debugging connection issues (e.g., bad URL, firewall).
        pytest.fail(f"Database connection failed: {e}")
    except Exception as e:
        # Catch any other unexpected exceptions
        pytest.fail(f"An unexpected error occurred during database connection test: {e}")