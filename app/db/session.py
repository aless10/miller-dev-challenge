import os
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from .db import Db

db_engine = Db(os.environ['DATABASE_URL'])


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with db_engine.get_session() as session:
        yield session
