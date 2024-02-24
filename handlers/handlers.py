import typing

from grpc.aio import AioRpcError

from client import grpc_todo_client
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from protos import todo_pb2_grpc, todo_pb2
from google.protobuf.json_format import MessageToDict

router = APIRouter()


@router.get("/{id}")
async def get_data(id: int, client: typing.Any = Depends(grpc_todo_client)):

    try:
        todo = await client.GetTodoId(todo_pb2.GetTodoIdRequest(id=id), timeout=5)
        return JSONResponse(MessageToDict(todo))
    except AioRpcError as ex:
        raise HTTPException(status_code=404, detail=ex.details())


@router.post("/")
async def create_todo(name: str,
                      completed: bool,
                      day: int,
                      client: typing.Any = Depends(grpc_todo_client)) -> JSONResponse:

    try:
        todo = await client.CreateTodo(todo_pb2.CreateTodoRequest(name=name, completed=completed, day=day), timeout=5)

        print(todo)
        return JSONResponse(MessageToDict(todo))
    except AioRpcError as ex:
        raise HTTPException(status_code=404, detail=ex.details())


@router.get('/todos')
async def get_list_todos(client: typing.Any = Depends(grpc_todo_client)) -> JSONResponse:
    try:
        todos = await client.ListTodos(todo_pb2.ListTodosRequest())
        return JSONResponse(MessageToDict(todos))
    except AioRpcError as ex:
        raise HTTPException(status_code=404, detail=ex.details())


@router.put('/')
async def update_todo(id: int, name: str, completed: bool, client: typing.Any = Depends(grpc_todo_client)):

    try:
        todo = await client.UpdateTodoId(todo_pb2.UpdateTodoIdRequest(id=id, name=name, completed=completed), timeout=5)
        return JSONResponse(MessageToDict(todo))
    except AioRpcError as ex:
        raise HTTPException(status_code=404, detail=ex.details())


@router.delete("/")
async def delete_todo(id: int, client: typing.Any = Depends(grpc_todo_client)):

    try:
        res = await client.DeleteTodoId(todo_pb2.DeleteTodoRequest(id=id))
        return JSONResponse(MessageToDict(res))
    except AioRpcError as ex:
        raise HTTPException(status_code=404, detail=ex.details())
