from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, BigInteger, ForeignKey
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base_model import Base


class TgChannel(Base):

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    deleted_at = Column(DateTime)
    tg_id = Column(BigInteger, index=True, unique=True)
    owner_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), onupdate="CASCADE", nullable=False)
    channel_url = Column(String)

    async def create(self, session: AsyncSession):
        session.add(self)
        await session.commit()

    async def delete(self, session: AsyncSession):
        self.deleted_at = datetime.now()
        await session.commit()

    @staticmethod
    async def get_channel_list(session: AsyncSession, owner_id: int):
        channels = await session.execute(select(TgChannel).where(TgChannel.owner_id == owner_id))
        return channels.scalars().all()
