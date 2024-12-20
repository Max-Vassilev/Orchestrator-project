import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import grpc
from concurrent import futures
from src.user_service.generated import user_service_pb2
from src.user_service.generated import user_service_pb2_grpc
from src.database.user_database import get_all_users_from_dynamodb, create_user_in_dynamodb

class UserService(user_service_pb2_grpc.UserServiceServicer):
    def GetAllUsers(self, request, context):
        users_from_db = get_all_users_from_dynamodb()
        user_response_list = []
        for user in users_from_db:
            user_response = user_service_pb2.User(
                name=user.Name, 
                email=user.Email
            )
            user_response_list.append(user_response)
        return user_service_pb2.GetUserResponse(users=user_response_list)

    def CreateUser(self, request, context):
        name = request.name
        email = request.email
        new_user = create_user_in_dynamodb(name, email)

        if new_user:
            context.set_details(f"User {name} created successfully")
            return user_service_pb2.CreateUserResponse()
        else:
            context.set_details("Error creating user")
            return user_service_pb2.CreateUserResponse()


server = grpc.server(futures.ThreadPoolExecutor())
user_service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
server.add_insecure_port('[::]:50051')
server.start()

print("User Service gRPC server is running on port 50051 ...")
server.wait_for_termination()
