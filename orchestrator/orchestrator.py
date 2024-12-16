from db.user_db import USER_DB
from models.user_model import User

def get_all_users() -> list[User]:
    return [User(**user_data) for user_data in USER_DB.values()]
