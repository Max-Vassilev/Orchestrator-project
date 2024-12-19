import grpc
from src.user_service.generated import user_service_pb2
from src.user_service.generated import user_service_pb2_grpc

def get_all_users_api():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_service_pb2_grpc.UserServiceStub(channel)
        response = stub.GetAllUsers(user_service_pb2.GetUserRequest())
        return response.users

def create_user_api(name: str, email: str):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_service_pb2_grpc.UserServiceStub(channel)
        request = user_service_pb2.CreateUserRequest(name=name, email=email)
        response = stub.CreateUser(request)
        return response
