from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.car import Car, CarOrm


async def get_cars(db_session: AsyncSession) -> list[Car]:
    query = select(CarOrm).all()
    query_result = await db_session.execute(query)
    return [Car.from_orm(getattr(row, CarOrm.__name__)) for row in query_result]


async def get_car(db_session: AsyncSession, car_id: str) -> Car | None:
    query = select(CarOrm).where(CarOrm.id == car_id)
    query_result = await db_session.execute(query)
    result = query_result.unique().first()
    return Car.from_orm(getattr(result, CarOrm.__name__)) if result is not None else None


async def add_car(db_session: AsyncSession, licence_plate: str, owner: str, daily_price: float) -> Car:
    car = CarOrm(licence_plate=licence_plate, owner=owner, daily_price=daily_price)
    db_session.add(car)
    await db_session.commit()
    await db_session.refresh(car)
    return Car.from_orm(car)


async def update_car(db_session: AsyncSession, car_id: str, new_daily_price: float) -> Car:
    query = update(CarOrm).where(CarOrm.id == car_id).values(daily_price=new_daily_price)
    await db_session.execute(query)
    await db_session.commit()
    updated_car = await get_car(db_session, car_id)
    await db_session.refresh(updated_car)
    return Car.from_orm(updated_car)


async def delete_car(db_session: AsyncSession, car_id: str) -> None:
    query = delete(CarOrm).where(CarOrm.id == car_id)
    transaction = await db_session.begin_nested()
    await db_session.execute(query)
    await transaction.commit()
