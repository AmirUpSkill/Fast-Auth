from sqlalchemy.orm import Session
from app.services.user_service import user_service
from app.schemas.user import UserCreate

def test_create_user(db_session: Session):
    """
    Test case for creating a new user.
    """
    user_in = UserCreate(
        name="Test User",
        email="test@example.com",
        avatar_url="http://example.com/avatar.png"
    )
    
    # --- Act ---
    created_user = user_service.create_user(db=db_session, user_in=user_in)
    
    # --- Assert ---
    assert created_user is not None
    assert created_user.email == user_in.email
    assert created_user.name == user_in.name
    assert created_user.id is not None
    assert created_user.created_at is not None

def test_get_user_by_email(db_session: Session):
    """
    Test case for retrieving a user by email.
    """
    # --- Arrange ---
    user_in = UserCreate(name="Jane Doe", email="jane.doe@example.com")
    user_service.create_user(db=db_session, user_in=user_in)
    
    # --- Act ---
    found_user = user_service.get_user_by_email(db=db_session, email="jane.doe@example.com")
    not_found_user = user_service.get_user_by_email(db=db_session, email="nobody@example.com")

    # --- Assert ---
    assert found_user is not None
    assert found_user.email == "jane.doe@example.com"
    assert not_found_user is None

def test_get_or_create_existing_user(db_session: Session):
    """
    Test the 'get' path of get_or_create: the user already exists.
    """
    # --- Arrange ---
    user_in = UserCreate(name="Existing User", email="existing@example.com")
    existing_user = user_service.create_user(db=db_session, user_in=user_in)
    
    # --- Act ---
    retrieved_user = user_service.get_or_create(db=db_session, user_in=user_in)

    # --- Assert ---
    assert retrieved_user is not None
    assert retrieved_user.id == existing_user.id
    assert retrieved_user.email == "existing@example.com"

def test_get_or_create_new_user(db_session: Session):
    """
    Test the 'create' path of get_or_create: the user does not exist.
    """
    # --- Arrange ---
    user_in = UserCreate(name="New User", email="new.user@example.com")

    # --- Act ---
    # User does not exist, so this should create them
    newly_created_user = user_service.get_or_create(db=db_session, user_in=user_in)
    
    # --- Assert ---
    assert newly_created_user is not None
    assert newly_created_user.id is not None
    assert newly_created_user.email == "new.user@example.com"
    
    # Verify it was actually added to the DB
    verified_user = user_service.get_user_by_email(db=db_session, email="new.user@example.com")
    assert verified_user is not None
    assert verified_user.id == newly_created_user.id