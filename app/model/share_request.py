import datetime
import uuid
import enum

from pydantic import BaseModel
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer, Enum, ForeignKeyConstraint
from sqlalchemy.orm import relationship

from .base import Base
from .car import CarOrm
from .user import UserOrm


class RequestStatus(enum.Enum):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REFUSED = 'refused'
    ACTIVE = 'active'
    ENDED = 'ended'


class ShareRequestInput(BaseModel):
    license_plate: str
    days: int

    class Config:
        orm_mode = True


class ShareRequestUpdateStatusInput(BaseModel):
    status: RequestStatus

    class Config:
        orm_mode = True


class ShareRequest(BaseModel):
    id: str
    license_plate: str
    requester: str
    days: int
    started_at: datetime.datetime | None = None
    ended_at: datetime.datetime | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    status: RequestStatus


class ShareRequestOrm(Base):
    __tablename__ = "share_request"
    id = Column(String(64), nullable=False, primary_key=True, default=lambda: str(uuid.uuid4()))
    license_plate = Column(String(200), ForeignKey(CarOrm.license_plate), nullable=False)
    requester = Column(String(200), ForeignKey(UserOrm.username), nullable=False)
    days = Column(Integer(), nullable=False)
    started_at = Column(DateTime(), nullable=True)
    ended_at = Column(DateTime(), nullable=True)
    created_at = Column(DateTime(), nullable=False, default=datetime.datetime.now())
    updated_at = Column(DateTime(), nullable=False, default=datetime.datetime.now())
    status = Column(Enum(RequestStatus))
