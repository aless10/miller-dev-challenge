import pytest
from app.repo import car as car_repo


@pytest.mark.asyncio
async def test_get_cars(db_session_no_car):
    result = await car_repo.get_cars(db_session_no_car)
    assert len(result) == 0


@pytest.mark.asyncio
async def test_add_car(db_session_no_car):
    result = await car_repo.add_car(db_session_no_car, license_plate='XY123ZZ', owner='test_user', daily_price=10,
                                    pick_up_place='Here', put_down_place='There')
    assert result.license_plate == 'XY123ZZ'
    result = await car_repo.get_cars(db_session_no_car)
    assert len(result) == 1


@pytest.mark.asyncio
async def test_update_car(db_session_car):
    updated_car = await car_repo.update_car(db_session_car, username='test_user_car', car_id='10866d4d-eee1-4c4e-bab7-885eb9d05f10', new_daily_price=12,
                                            new_pick_up_place='Here', new_put_down_place='There')
    assert updated_car.daily_price == 12


@pytest.mark.asyncio
async def test_update_car_different_owner(db_session_car):
    updated_car = await car_repo.update_car(db_session_car, username='another-user', car_id='10866d4d-eee1-4c4e-bab7-885eb9d05f10', new_daily_price=12,
                                            new_pick_up_place='Here', new_put_down_place='There')
    assert updated_car is None


@pytest.mark.asyncio
async def test_delete_car(db_session_car):
    """We first try to delete a car with a different owner, then we delete the one with the correct owner"""

    await car_repo.delete_car(db_session_car, car_id='10866d4d-eee1-4c4e-bab7-885eb9d05f10', username='another_user')
    assert await car_repo.get_car(db_session_car, car_id='10866d4d-eee1-4c4e-bab7-885eb9d05f10') is not None

    await car_repo.delete_car(db_session_car, car_id='10866d4d-eee1-4c4e-bab7-885eb9d05f10', username='test_user_car')
    assert await car_repo.get_car(db_session_car, car_id='10866d4d-eee1-4c4e-bab7-885eb9d05f10') is None

