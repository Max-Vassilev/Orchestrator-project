import strawberry
from models.user_model import User
from orchestrator.orchestrator import get_all_users

@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> list[User]:
        return get_all_users()

schema = strawberry.Schema(query=Query)
