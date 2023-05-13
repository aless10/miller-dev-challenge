from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from ..model.base import Base


class Db:
    def __init__(self, url: str, echo: bool = True, **kwargs: Any) -> None:
        self.engine = create_async_engine(url, echo=echo, future=True, **kwargs)
        self.session_factory = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False, future=True
        )

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            try:
                yield session
            finally:
                await session.close()

    async def create_all(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
