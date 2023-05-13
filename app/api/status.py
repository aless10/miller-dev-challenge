from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def status() -> dict:
    return {"alive": True}
