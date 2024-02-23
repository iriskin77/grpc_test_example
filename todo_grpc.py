from services.todo import run_server
from core.settings import TODO_GRPC_SERVER_ADDR
import asyncio


if __name__ == '__main__':
    asyncio.run(run_server(TODO_GRPC_SERVER_ADDR))
