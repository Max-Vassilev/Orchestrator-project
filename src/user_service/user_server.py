import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


import grpc
from concurrent import futures
from src.user_service.generated import user_service_pb2
from src.user_service.generated import user_service_pb2_grpc
from src.database.user_database import get_all_users_from_dynamodb


class UserService(user_service_pb2_grpc.UserServiceServicer):
    def GetAllUsers(self, request, context):
        users = get_all_users_from_dynamodb()
        return user_service_pb2.UserResponse(users=[user_service_pb2.User(name=user.Name, email=user.Email) for user in users])

server = grpc.server(futures.ThreadPoolExecutor())
user_service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
server.add_insecure_port('[::]:50051')
server.start()

print("User Service gRPC server is running on port 50051 ...")
server.wait_for_termination()
