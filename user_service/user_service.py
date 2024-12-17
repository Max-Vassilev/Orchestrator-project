from user_service.database.user_database import get_all_users_from_dynamodb

def get_all_users_service() -> list:
    return get_all_users_from_dynamodb()
