from fastapi import APIRouter
from handlers import todo, approver

routes = APIRouter()


routes.include_router(router=todo.router, prefix="/todo")
routes.include_router(router=approver.router, prefix="/approver")
