import pytest

from app.repo import user as user_repo


@pytest.mark.asyncio
async def test_get_user(db_session):
    result = await user_repo.get_user(db_session, username='not found')
    assert result is None


@pytest.mark.asyncio
async def test_add_user(db_session):
    result = await user_repo.add_user(db_session, username='test', password='test_password')
    assert result.username == 'test'
    assert await user_repo.get_user(db_session, 'test') is not None
