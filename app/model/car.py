import uuid

from pydantic import BaseModel
from sqlalchemy import Column, String, ForeignKey, Float

from .base import Base
from .user import UserOrm


class Car(BaseModel):
    id: str
    license_plate: str
    owner: str
    daily_price: float

    class Config:
        orm_mode = True


class CarOrm(Base):
    __tablename__ = "car"
    id = Column(String(64), nullable=False, primary_key=True, default=lambda: str(uuid.uuid4()))
    license_plate = Column(String(200), nullable=False, primary_key=True)
    owner = Column(String(200), ForeignKey(UserOrm.username), nullable=False)
    daily_price = Column(Float(), nullable=False)
