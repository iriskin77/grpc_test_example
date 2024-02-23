from fastapi import APIRouter
from handlers import handlers

routes = APIRouter()


routes.include_router(router=handlers.router, prefix="/test")
