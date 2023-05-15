from fastapi import APIRouter

from . import status, auth, car, share_request

api_router = APIRouter(prefix="/api")
api_router.include_router(
    status.router, prefix="/status", tags=["status"]
)

api_router.include_router(
    auth.router, prefix="", tags=["auth"]
)

api_router.include_router(
    car.router, prefix="/cars", tags=["cars"]
)

api_router.include_router(
    share_request.router, prefix="/requests", tags=["requests"]
)

