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
    result = await car_repo.add_car(db_session, license_plate='AB123CD', owner='test_user', daily_price=10,
                                    pick_up_place='Here', put_down_place='There')
    assert result.license_plate == 'AB123CD'
    result = await car_repo.get_cars(db_session)
    assert len(result) == 1


@pytest.mark.asyncio
async def test_update_car(db_session, add_user):
    car = await car_repo.add_car(db_session, license_plate='AB123CD', owner='test_user', daily_price=10,
                                 pick_up_place='Here', put_down_place='There')
    updated_car = await car_repo.update_car(db_session, username='test_user', car_id=car.id, new_daily_price=12,
                                            new_pick_up_place='Here', new_put_down_place='There')
    assert updated_car.daily_price == 12


@pytest.mark.asyncio
async def test_update_car_different_owner(db_session, add_user):
    car = await car_repo.add_car(db_session, license_plate='AB123CD', owner='test_user', daily_price=10,
                                 pick_up_place='Here', put_down_place='There')
    updated_car = await car_repo.update_car(db_session, username='another-user', car_id=car.id, new_daily_price=12,
                                            new_pick_up_place='Here', new_put_down_place='There')
    assert updated_car is None


@pytest.mark.asyncio
async def test_delete_car(db_session, add_user):
    car = await car_repo.add_car(db_session, license_plate='AB123CD', owner='test_user', daily_price=10,
                                 pick_up_place='Here', put_down_place='There')
    await car_repo.delete_car(db_session, car_id=car.id, username='test_user')
    assert await car_repo.get_car(db_session, car_id=car.id) is None


@pytest.mark.asyncio
async def test_delete_car_different_owner(db_session, add_user):
    car = await car_repo.add_car(db_session, license_plate='AB123CD', owner='test_user', daily_price=10,
                                 pick_up_place='Here', put_down_place='There')
    await car_repo.delete_car(db_session, car_id=car.id, username='another_user')
    assert await car_repo.get_car(db_session, car_id=car.id) is not None
