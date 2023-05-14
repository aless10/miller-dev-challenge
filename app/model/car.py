import uuid

from pydantic import BaseModel
from sqlalchemy import Column, String, ForeignKey, Float

from .base import Base
from .user import UserOrm


class CarInput(BaseModel):
    license_plate: str
    daily_price: float
    pick_up_place: str
    put_down_place: str


class Car(BaseModel):
    id: str
    license_plate: str
    owner: str
    daily_price: float
    pick_up_place: str
    put_down_place: str

    class Config:
        orm_mode = True


class CarOrm(Base):
    __tablename__ = "car"
    id = Column(String(64), nullable=False, primary_key=True, default=lambda: str(uuid.uuid4()))
    license_plate = Column(String(200), nullable=False, unique=True)
    owner = Column(String(200), ForeignKey(UserOrm.username), nullable=False)
    daily_price = Column(Float(), nullable=False)
    pick_up_place = Column(String(200), nullable=False)
    put_down_place = Column(String(200), nullable=False)
