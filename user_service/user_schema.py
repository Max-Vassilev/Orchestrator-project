import strawberry
from orchestrator.orchestrator import get_user
from models.user_model import User
from db.user_db import USER_DB

@strawberry.type
class Query:
    @strawberry.field
    def user(self, info, user_id: str) -> User:
        return get_user(user_id)
    
    @strawberry.field
    def users(self, info) -> list[User]:
        return [User(**user_data) for user_data in USER_DB.values()]
    
schema = strawberry.Schema(query=Query)
