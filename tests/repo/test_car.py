import pytest
import pytest_asyncio

from app.repo import car as car_repo, user as user_repo


@pytest_asyncio.fixture(scope="session")
async def add_user(db_session):
    await user_repo.add_user(db_session, username='test_user', password='test')


@pytest.mark.asyncio
async def test_get_cars(db_session, add_user):
    result = await car_repo.get_cars(db_session)
    assert len(result) == 0


@pytest.mark.asyncio
async def test_add_car(db_session, add_user):
    result = await car_repo.add_car(db_session, license_plate='AB123CD', owner='test_user', daily_price=10)
    assert result.license_plate == 'AB123CD'
    result = await car_repo.get_cars(db_session)
    assert len(result) == 1


@pytest.mark.asyncio
async def test_update_car(db_session, add_user):
    car = await car_repo.add_car(db_session, license_plate='AB123CD', owner='test_user', daily_price=10)
    updated_car = await car_repo.update_car(db_session, car_id=car.id, new_daily_price=12)
    assert updated_car.daily_price == 12


@pytest.mark.asyncio
async def test_delete_car(db_session, add_user):
    car = await car_repo.add_car(db_session, license_plate='AB123CD', owner='test_user', daily_price=10)
    await car_repo.delete_car(db_session, car_id=car.id)
    assert await car_repo.get_car(db_session, car_id=car.id) is None
