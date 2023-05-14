from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.car import Car, CarOrm


async def get_cars(db_session: AsyncSession) -> list[Car]:
    query = select(CarOrm)
    query_result = await db_session.execute(query)
    return [Car.from_orm(getattr(row, CarOrm.__name__)) for row in query_result]


async def get_car(db_session: AsyncSession, car_id: str) -> Car | None:
    query = select(CarOrm).where(CarOrm.id == car_id)
    query_result = await db_session.execute(query)
    result = query_result.unique().first()
    return Car.from_orm(getattr(result, CarOrm.__name__)) if result is not None else None


async def get_car_by_license(db_session: AsyncSession, license_plate: str) -> Car | None:
    query = select(CarOrm).where(CarOrm.license_plate == license_plate)
    query_result = await db_session.execute(query)
    result = query_result.unique().first()
    return Car.from_orm(getattr(result, CarOrm.__name__)) if result is not None else None


async def add_car(
        db_session: AsyncSession,
        license_plate: str,
        owner: str,
        daily_price: float,
        pick_up_place: str,
        put_down_place: str
) -> Car:
    car = CarOrm(
        license_plate=license_plate,
        owner=owner,
        daily_price=daily_price,
        pick_up_place=pick_up_place,
        put_down_place=put_down_place
    )
    db_session.add(car)
    await db_session.commit()
    await db_session.refresh(car)
    return Car.from_orm(car)


async def update_car(
        db_session: AsyncSession,
        username: str,
        car_id: str,
        new_daily_price: float,
        new_pick_up_place: str,
        new_put_down_place: str,
) -> Car | None:
    query = update(CarOrm) \
        .where(CarOrm.id == car_id, CarOrm.owner == username) \
        .values(
        daily_price=new_daily_price,
        pick_up_place=new_pick_up_place,
        put_down_place=new_put_down_place,
    )
    result = await db_session.execute(query)
    if result.rowcount > 0:
        await db_session.commit()
        updated_car = await get_car(db_session, car_id)
        return Car.from_orm(updated_car)
    return


async def delete_car(db_session: AsyncSession, username: str, car_id: str) -> None:
    query = delete(CarOrm).where(CarOrm.id == car_id, CarOrm.owner == username)
    await db_session.execute(query)
    await db_session.commit()
