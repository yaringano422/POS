# services/users.py
from sqlalchemy.orm import Session
from ..data.models import User

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username: str, role: str):
        user = User(username=username, role=role)
        self.db.add(user)
        self.db.commit()