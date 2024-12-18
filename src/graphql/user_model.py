import strawberry

@strawberry.type
class User:
    Name: str
    Email: str