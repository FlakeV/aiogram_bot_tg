import asyncio
import logging

from aiogram import Dispatcher
from aiogram.methods import DeleteWebhook

from app import bot
from handlers import ROUTERS


dp = Dispatcher()

for router in ROUTERS:
    dp.include_router(router)


async def main():
    logging.info("Bot start")
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot start")
    asyncio.run(main())
