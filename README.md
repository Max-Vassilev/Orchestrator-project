## Project Architecture

The system follows the structure below:

- **GraphQL**: Frontend communication layer
- **Orchestrator**: Manages the communication between the frontend and backend services
- **User Service**: Handles user management and communicates with the database via gRPC
- **DynamoDB**: NoSQL database for storing user data

The flow is as follows:

GraphQL ----> Orchestrator ----> User Service --gRPC--> DynamoDB
