from typing import Annotated

from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.auth import get_current_active_user
from app.db.session import get_session
from app.model.car import Car
from app.model.user import User
from app.repo import car as car_repo

router = APIRouter()


@router.get("", response_model=list[Car])
async def get_cars(
        current_user: Annotated[User, Depends(get_current_active_user)],
        db_session: AsyncSession = Depends(get_session),
):
    return await car_repo.get_cars(db_session)


@router.post("")
async def add_car(
        current_user: Annotated[User, Depends(get_current_active_user)],
        db_session: AsyncSession = Depends(get_session),
):
    new_car = await car_repo.add_car(db_session, 'hello', current_user.username, 10.0)
    return new_car


@router.put("/update/{car_id}")
async def update_car(
        car_id: str,
        current_user: Annotated[User, Depends(get_current_active_user)],
        db_session: AsyncSession = Depends(get_session),
):
    await car_repo.update_car(db_session, car_id, 12)
    return


@router.delete("/delete/{car_id}")
async def delete_car(
        car_id: str,
        current_user: Annotated[User, Depends(get_current_active_user)],
        db_session: AsyncSession = Depends(get_session),
):
    await car_repo.delete_car(db_session, car_id)
    return
