# tests/test_users.py
import pytest
from services.users import UserService
from data.models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data.database import Base

@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    yield Session()

def test_create_user(db_session):
    service = UserService(db_session)
    service.create_user("admin", "admin")

    users = db_session.query(User).all()
    assert len(users) == 1
    assert users[0].username == "admin"
    assert users[0].role == "admin"