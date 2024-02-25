import grpc
from grpc import aio
from protos import approver_pb2_grpc, approver_pb2
from handlers.models import Todo
from google.protobuf import wrappers_pb2 as _wrappers_pb2

WORK_DAY = (1, 2, 3, 4, 5)

class ApproverService(approver_pb2_grpc.ApproverServiceServicer):

    def GetApprover(self, request, context):

        if request.day in WORK_DAY:
            status = True
        else:
            status = False
        return approver_pb2.GetApproverResponse(approver={"status": _wrappers_pb2.BoolValue(value=status)})


async def run_server(address):
    # Здесь получаем асинхронный сервер
    await Todo.create_table(if_not_exists=True)
    server = aio.server()
    print('START APPROVER SERVER')
    # Регистрируем наш ApproverService сервер в aio сервере
    approver_pb2_grpc.add_ApproverServiceServicer_to_server(ApproverService(), server)
    # Теперь этот сервер необходимо зарегистрировать по какому-то адресу
    server.add_insecure_port(address)
    print('START APPROVER SERVER')
    await server.start()
    await server.wait_for_termination()



