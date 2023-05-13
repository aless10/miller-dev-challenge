from fastapi import APIRouter

from . import status, auth, car

api_router = APIRouter()
api_router.include_router(
    status.router, prefix="/status", tags=["status"]
)

api_router.include_router(
    auth.router, prefix="", tags=["auth"]
)

api_router.include_router(
    car.router, prefix="/cars", tags=["cars"]
)
