from strawberry.asgi import GraphQL
from src.graphql.schema import schema

graphql_app = GraphQL(schema)
