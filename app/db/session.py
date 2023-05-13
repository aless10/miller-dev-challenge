from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

connector = DBConnector(settings.DB_URL.get_secret_value())


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with connector.get_session() as session:
        yield session
