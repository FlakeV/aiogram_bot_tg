import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app import session
from models import User
from keyboards.main_keyboard import main_keyboard

user_start_handler_router = Router()


@user_start_handler_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.clear()
    logging.info(f"USER with id {message.from_user.id}, join bot")
    user = await User.get(session, message.from_user.id)
    if not user:
        new_user = User(
            tg_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            username=message.from_user.username,
        )
        await new_user.create(session)

    keyboard = await main_keyboard(user.admin)

    await message.answer(f"Hello, {message.from_user.full_name}!", reply_markup=keyboard)
