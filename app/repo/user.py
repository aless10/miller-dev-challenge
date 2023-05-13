from sqlalchemy import select
from app.model.user import UserOrm, User


async def get_user(db_session, username: str) -> User | None:
    query = select(UserOrm).where(UserOrm.username == username)
    query_result = await db_session.execute(query)
    result = query_result.first()
    return User.from_orm(**result) if result is not None else None
