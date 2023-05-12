from fastapi import APIRouter

from . import status

api_router = APIRouter()
api_router.include_router(
    status.router, prefix="/status", tags=["status"]
)
