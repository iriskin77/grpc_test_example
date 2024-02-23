from core.async_session import get_async_session
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()


@router.get("/")
async def get_data():
    return {"message": 'Hello world'}
