from db.user_db import USER_DB
from models.user_model import User

def get_user(user_id: str) -> User:
    user_data = USER_DB.get(user_id)
    return User(**user_data) if user_data else None
