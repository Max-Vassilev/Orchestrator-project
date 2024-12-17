from user_database.user_db import get_all_users_from_dynamodb
from user_service.user_model import User

def get_all_users() -> list[User]:
    return get_all_users_from_dynamodb()
