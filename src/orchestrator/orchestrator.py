from src.user_service.user_api import get_all_users_api, create_user_api
from src.graphql.user_model import User

def get_all_users() -> list[User]:
    users = get_all_users_api()
    return [User(Name=user.name, Email=user.email) for user in users]

def create_user(name: str, email: str) -> User:
    response = create_user_api(name, email)
    if response:
        return User(Name=name, Email=email)
    return None
