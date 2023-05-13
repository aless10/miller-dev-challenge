from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()


@router.get("")
async def status() -> dict:
    return {"alive": True}
