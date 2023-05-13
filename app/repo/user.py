from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.user import UserOrm, User


async def get_user(db_session: AsyncSession, username: str) -> User | None:
    query = select(UserOrm).where(UserOrm.username == username)
    query_result = await db_session.execute(query)
    result = query_result.unique().first()
    return User.from_orm(getattr(result, UserOrm.__name__)) if result is not None else None


async def add_user(db_session: AsyncSession, username: str, password) -> User:
    user = UserOrm(username=username, password=password)
    db_session.add(user)
    await db_session.commit()
    await db_session.refresh(user)
    return User.from_orm(user)
