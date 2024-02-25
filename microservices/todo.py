from grpc import aio
from protos import todo_pb2_grpc, approver_pb2_grpc, approver_pb2
from protos import todo_pb2
from handlers.models import Todo
from client import grpc_todo_approver


class TodoService(todo_pb2_grpc.TodoServiceServicer):
    # create todo
    async def CreateTodo(self, request, context):

        todo = await Todo.insert(
            Todo(name=request.name, completed=request.completed, day=request.day)
        )

        print(todo)
        print("CreateTodo")

        return todo_pb2.CreateTodoResponse(todo=todo[0])

    async def ListTodos(self, request, context):
        todo = await Todo.select()
        print(todo)
        print('ListTodos')
        return todo_pb2.ListTodosResponse(todos=todo)

    async def GetTodoId(self, request, context):

        todo = await Todo.select().where(Todo.id == request.id).first()
        print("GetTodoId")
        return todo_pb2.GetTodoIdResponse(todo=todo)

    async def UpdateTodoId(self, request, context):

        await Todo.update({Todo.name: request.name, Todo.completed: request.completed}).where(Todo.id == request.id)

        todo = await Todo.select().where(Todo.id == request.id).first()
        print("UpdateTodo")
        return todo_pb2.UpdateTodoIdResponse(todo=todo)

    async def DeleteTodoId(self, request, context):

        await Todo.delete().where(Todo.id == request.id)
        print('DeleteTodoId')
        return todo_pb2.DeleteTodoResponse(success=True)

    async def GetTodoApprover(self, request, context):

        todo = await Todo.select().where(Todo.id == request.id).first()
        print('GetTodoApprover')

        if todo:
            # Подключаемся к клиенту сервиса Approver
            client = await grpc_todo_approver()
            # Отправляем ему запрос (реализуем метод ApproverService из approver.proto)
            req = await client.GetApprover(approver_pb2.GetApproverRequest(day=todo['day']), timeout=5)

            return todo_pb2.GetTodoApproverResponse(todo=todo, approver=req.approver)

        else:
            return todo_pb2.GetTodoApproverResponse(todo=None, approver=None)


async def run_server(address):
    # Здесь получаем асинхронный сервер
    await Todo.create_table(if_not_exists=True)
    server = aio.server()
    print('START SERVER')
    # Регистрируем наш Todo сервер в aio сервере
    todo_pb2_grpc.add_TodoServiceServicer_to_server(TodoService(), server)
    # Теперь этот сервер необходимо зарегистрировать по какому-то адресу
    server.add_insecure_port(address)
    print('START SERVER')
    await server.start()
    await server.wait_for_termination()


#asyncio.run(run_server('0.0.0.0:50051'))
