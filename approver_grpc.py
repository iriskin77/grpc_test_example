from microservices.approver import run_server
from core.settings import APPROVER_GRPC_SERVER_ADDR
import asyncio


if __name__ == '__main__':
    asyncio.run(run_server(APPROVER_GRPC_SERVER_ADDR))
