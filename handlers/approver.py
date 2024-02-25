import typing
from grpc.aio import AioRpcError
from client import grpc_todo_client
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from protos import todo_pb2_grpc, todo_pb2
from google.protobuf.json_format import MessageToDict


router = APIRouter()


@router.get("/{id}")
async def approve_todo(id: int, client: typing.Any = Depends(grpc_todo_client)) -> JSONResponse:

    try:
        todo = await client.GetTodoApprover(todo_pb2.GetTodoIdRequest(id=id), timeout=5)
    except AioRpcError as ex:
        raise HTTPException(status_code=404, detail=ex.details())

    return JSONResponse(MessageToDict(todo))
