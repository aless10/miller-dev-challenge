import asyncio
import os
from collections.abc import Generator, AsyncGenerator

import pytest
import pytest_asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.testclient import TestClient

from app.model.base import Base

os.environ['DATABASE_URL'] = "sqlite+aiosqlite:///:memory:"
os.environ["SECRET_KEY"] = "testsecretkey"

from app.db.session import db_engine
from app.main import app


@pytest.fixture(scope="session")
def app_client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


async def get_test_db_session():
    async with db_engine.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with db_engine.get_session() as session:
        yield session


@pytest_asyncio.fixture(scope="session")
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    session_maker = get_test_db_session()
    async for async_sqlite_session in session_maker:
        yield async_sqlite_session


@pytest_asyncio.fixture(scope="session")
async def db_session_no_car() -> AsyncGenerator[AsyncSession, None]:
    session_maker = get_test_db_session()
    async for async_sqlite_session in session_maker:
        await async_sqlite_session.execute(
            text("""
                    INSERT INTO user (username, password)
                    VALUES ('test_user', 'testpassword');
                    """)
        )
        await async_sqlite_session.commit()
        yield async_sqlite_session


@pytest_asyncio.fixture(scope="session")
async def db_session_car() -> AsyncGenerator[AsyncSession, None]:
    session_maker = get_test_db_session()
    async for async_sqlite_session in session_maker:
        await async_sqlite_session.execute(
            text("""
            INSERT INTO user (username, password)
            VALUES ('test_user_car', 'testpassword');
            """)
        )
        await async_sqlite_session.execute(
            text("""
                    INSERT INTO car (id, license_plate, owner, daily_price, pick_up_place, put_down_place)
                    VALUES ('10866d4d-eee1-4c4e-bab7-885eb9d05f10', 'AB123CD', 'test_user_car', 10.0, 'Here', 'There');
                    """)
        )
        await async_sqlite_session.commit()
        yield async_sqlite_session
