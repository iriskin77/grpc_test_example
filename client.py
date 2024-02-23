import grpc
from protos import todo_pb2_grpc as pb2_grpc
from core.settings import TODO_GRPC_SERVER_ADDR


async def grpc_todo_client():
    # Открываем канал и указываем, на каком порту
    channel = grpc.aio.insecure_channel(TODO_GRPC_SERVER_ADDR)
    # Создаем и возвращаем клиент
    client = pb2_grpc.TodoServiceStub(channel)
    return client
