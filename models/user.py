from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, BigInteger, Boolean
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base_model import Base


class User(Base):

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    deleted_at = Column(DateTime)
    tg_id = Column(BigInteger, index=True, unique=True)
    admin = Column(Boolean, default=False)

    def __repr__(self):
        return f"Name: {self.first_name} {self.last_name}, tg_id={self.tg_id}"

    async def create(self, session: AsyncSession) -> None:
        session.add(self)
        await session.commit()

    async def delete(self, session: AsyncSession) -> None:
        self.deleted_at = datetime.now()
        await session.commit()

    @staticmethod
    async def set_admin_status_to_user(session: AsyncSession, user: "User", admin: bool) -> None:
        user.admin = admin
        await session.commit()

    @staticmethod
    async def get(session: AsyncSession, tg_id: int) -> "User":
        user = await session.execute(select(User).where(User.tg_id == tg_id))
        return user.scalars().one_or_none()

    @staticmethod
    async def get_all_admins(session: AsyncSession) -> list["User"]:
        admins = await session.execute(select(User).where(User.admin == True))
        return admins.scalars().all()
