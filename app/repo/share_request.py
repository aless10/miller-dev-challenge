from sqlalchemy import select, update, delete, or_
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.share_request import ShareRequestOrm, ShareRequest, RequestStatus
from .car import get_car_by_license
from ..model.car import Car, CarOrm


async def get_requests_as_owner(db_session: AsyncSession, owner: str) -> list[ShareRequest]:
    query = select(ShareRequestOrm) \
        .join(CarOrm, CarOrm.license_plate == ShareRequestOrm.license_plate) \
        .where(CarOrm.owner == owner)
    query_result = await db_session.execute(query)
    return [ShareRequest.from_orm(getattr(row, ShareRequest.__name__)) for row in query_result]


async def get_requests_as_requester(db_session: AsyncSession, requester: str) -> list[ShareRequest]:
    query = select(ShareRequestOrm).where(ShareRequestOrm.requester == requester)
    query_result = await db_session.execute(query)
    return [ShareRequest.from_orm(getattr(row, ShareRequest.__name__)) for row in query_result]


async def get_request(db_session: AsyncSession, request_id: str) -> ShareRequest | None:
    query = select(ShareRequestOrm).where(ShareRequestOrm.id == request_id)
    query_result = await db_session.execute(query)
    result = query_result.unique().first()
    return ShareRequest.from_orm(getattr(result, ShareRequestOrm.__name__)) if result is not None else None


async def get_available_cars(db_session: AsyncSession, owner: str) -> list[Car]:
    query = select(
        CarOrm.id,
        CarOrm.owner,
        CarOrm.license_plate,
        CarOrm.daily_price,
        CarOrm.pick_up_place,
        CarOrm.put_down_place
    ) \
        .join(ShareRequestOrm, isouter=True) \
        .where(
        CarOrm.owner != owner,
        or_(
            ShareRequestOrm.status.not_in([RequestStatus.PENDING, RequestStatus.ACTIVE, RequestStatus.ACCEPTED]),
            ShareRequestOrm.id.is_(None)
            )
    )
    query_result = await db_session.execute(query)
    return [Car.from_orm(row) for row in query_result]


async def add_request(
        db_session: AsyncSession,
        license_plate: str,
        requester: str,
        days: int
) -> ShareRequest:
    requested_car = await get_car_by_license(db_session, license_plate)
    share_request = ShareRequestOrm(
        license_plate=license_plate,
        owner=requested_car.owner,
        requester=requester,
        days=days,
        status=RequestStatus.PENDING
    )
    db_session.add(share_request)
    await db_session.commit()
    await db_session.refresh(share_request)
    return ShareRequest.from_orm(share_request)


async def update_request(
        db_session: AsyncSession,
        owner: str,
        request_id: str,
        status: str,
) -> ShareRequest | None:
    query = update(ShareRequestOrm) \
        .where(ShareRequestOrm.id == request_id, ShareRequestOrm.owner == owner) \
        .values(
        status=RequestStatus(status),
    )
    result = await db_session.execute(query)
    if result.rowcount > 0:
        await db_session.commit()
        updated_car = await get_request(db_session, request_id)
        return ShareRequest.from_orm(updated_car)
    return


async def delete_request(db_session: AsyncSession, requester: str, request_id: str) -> None:
    query = delete(ShareRequestOrm).where(ShareRequestOrm.id == request_id, ShareRequestOrm.requester == requester)
    await db_session.execute(query)
    await db_session.commit()
