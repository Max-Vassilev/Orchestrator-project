import grpc
from proto import user_service_pb2
from proto import user_service_pb2_grpc
from src.graphql.user_model import User

def get_all_users() -> list[User]:
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_service_pb2_grpc.UserServiceStub(channel)
        response = stub.GetAllUsers(user_service_pb2.UserRequest())
        return [User(Name=user.name, Email=user.email) for user in response.users]
