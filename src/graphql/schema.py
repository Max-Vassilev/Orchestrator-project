import strawberry
from src.graphql.user_model import User
from src.orchestrator.orchestrator import get_all_users

@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> list[User]:
        return get_all_users()

schema = strawberry.Schema(query=Query)
