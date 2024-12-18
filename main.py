import uvicorn
from src.graphql.graphql_server import graphql_app

if __name__ == "__main__":
    uvicorn.run(graphql_app, host="0.0.0.0", port=8000)
