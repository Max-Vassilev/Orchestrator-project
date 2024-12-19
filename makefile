# generate_grpc_code:
	python -m grpc_tools.protoc -I./proto --python_out=./src/user_service/generated --grpc_python_out=./src/user_service/generated proto/user_service.proto

start_user_service:
	python src/user_service/user_server.py

start_orchestrator:
	python main.py
