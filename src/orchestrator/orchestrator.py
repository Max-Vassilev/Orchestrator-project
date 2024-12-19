from src.user_service.user_api import get_all_users_api
from src.graphql.user_model import User

def get_all_users() -> list[User]:
    users = get_all_users_api()
    return [User(Name=user.name, Email=user.email) for user in users]
