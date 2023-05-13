from typing import Annotated

from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.auth import get_current_active_user
from app.db.session import get_session
from app.model.car import Car, CarInput
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
        car: CarInput,
        current_user: Annotated[User, Depends(get_current_active_user)],
        db_session: AsyncSession = Depends(get_session),
):
    print(car)
    new_car = await car_repo.add_car(db_session, car.license_plate, current_user.username, car.daily_price)
    return new_car


@router.put("/update/{car_id}")
async def update_car(
        car_id: str,
        car: CarInput,
        current_user: Annotated[User, Depends(get_current_active_user)],
        db_session: AsyncSession = Depends(get_session),
):
    await car_repo.update_car(db_session, car_id, car.daily_price)
    return


@router.delete("/delete/{car_id}")
async def delete_car(
        car_id: str,
        current_user: Annotated[User, Depends(get_current_active_user)],
        db_session: AsyncSession = Depends(get_session),
):
    await car_repo.delete_car(db_session, car_id)
    return
