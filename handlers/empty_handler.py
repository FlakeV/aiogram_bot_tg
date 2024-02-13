from aiogram import Router
from aiogram.types import Message


empty_handler_router = Router()


@empty_handler_router.message()
async def empty_handler(message: Message):
    await message.answer(
        "Unknown command",
    )
