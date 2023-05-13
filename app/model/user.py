from pydantic import BaseModel
from sqlalchemy import Column, String

from .base import Base


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    password: str


class UserOrm(Base):
    __tablename__ = "user"
    username = Column(String(200), nullable=False, primary_key=True)
    password = Column(String(200), nullable=False)
