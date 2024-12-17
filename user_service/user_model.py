import strawberry

@strawberry.type
class User:
    Name: str
    Email: str
    Age: int

    def __init__(self, Name, Email, Age):
        self.Name = Name
        self.Email = Email
        self.Age = Age