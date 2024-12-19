import strawberry
from src.graphql.user_model import User
from src.orchestrator.orchestrator import get_all_users, create_user

@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> list[User]:
        return get_all_users()
    
@strawberry.type
class Mutation:
    @strawberry.field
    def create_user(self, name: str, email: str) -> User:
        return create_user(name, email)

schema = strawberry.Schema(query=Query, mutation=Mutation)