from typing import Annotated

from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from app.api.auth import get_current_active_user
from app.db.session import get_session
from app.model.car import Car
from app.model.share_request import ShareRequest, ShareRequestInput, ShareRequestUpdateStatusInput
from app.model.user import User
from app.repo import share_request as share_request_repo

router = APIRouter()


@router.get("/owner", response_model=list[ShareRequest])
async def get_requests_as_owner(
        current_user: Annotated[User, Depends(get_current_active_user)],
        db_session: AsyncSession = Depends(get_session),
):
    return await share_request_repo.get_requests_as_owner(db_session, current_user.username)


@router.get("/requester", response_model=list[ShareRequest])
async def get_requests_as_requester(
        current_user: Annotated[User, Depends(get_current_active_user)],
        db_session: AsyncSession = Depends(get_session),
):
    return await share_request_repo.get_requests_as_requester(db_session, current_user.username)


@router.get("/available-cars", response_model=list[Car])
async def get_available_cars(
        current_user: Annotated[User, Depends(get_current_active_user)],
        db_session: AsyncSession = Depends(get_session),
):
    return await share_request_repo.get_available_cars(db_session, current_user.username)


@router.post("", response_model=ShareRequest, status_code=HTTP_201_CREATED)
async def add_request(
        share_request: ShareRequestInput,
        current_user: Annotated[User, Depends(get_current_active_user)],
        db_session: AsyncSession = Depends(get_session),
):
    return await share_request_repo.add_request(
        db_session,
        share_request.license_plate,
        current_user.username,
        share_request.days,
    )


@router.put("/update/{request_id}", status_code=HTTP_204_NO_CONTENT)
async def update_request(
        request_id: str,
        request_status: ShareRequestUpdateStatusInput,
        current_user: Annotated[User, Depends(get_current_active_user)],
        db_session: AsyncSession = Depends(get_session),
):
    await share_request_repo.update_request(
        db_session,
        current_user.username,
        request_id,
        request_status.status.value
    )
    return


@router.delete("/delete/{request_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_request(
        request_id: str,
        current_user: Annotated[User, Depends(get_current_active_user)],
        db_session: AsyncSession = Depends(get_session),
):
    await share_request_repo.delete_request(db_session, current_user.username, request_id)
    return
