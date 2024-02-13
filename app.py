import logging
import datetime

from aiogram import Bot

from configs.config import app_config

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(app_config.db_url, echo=True)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession, future=True)
session = async_session()

logging.basicConfig(
    level=app_config.log_level,
    filename=f"logs/bot_log_{datetime.date.today()}.log",
    filemode="a",
)

bot = Bot(token=app_config.bot_token)
