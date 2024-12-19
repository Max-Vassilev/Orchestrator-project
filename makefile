# generate_grpc_code:
# 	python -m grpc_tools.protoc -I./proto --python_out=./src/user_service --grpc_python_out=./src/user_service proto/user_service.proto

start_user_service:
	python src/user_service/user_service.py

start_orchestrator:
	python main.py
