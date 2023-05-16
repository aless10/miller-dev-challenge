import pytest
from app.repo import user as user_repo


@pytest.mark.asyncio
async def test_signup_ok(app_client, db_session):
    username = 'newUser'
    password = 'passwordUser'
    response = app_client.post(
        "/api/signup",
        data={"username": username, "password": password},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == 200
    assert response.json()['token_type'] == 'bearer'
    assert await user_repo.get_user(db_session, username) is not None
