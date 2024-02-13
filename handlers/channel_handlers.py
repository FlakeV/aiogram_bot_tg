from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
import validators

from app import session
from models import User, TgChannel
from states import ManageChannelList

chanel_handler_router = Router()


@chanel_handler_router.message(F.text == "Мои каналы")
async def my_channel_handler(message: Message, state: FSMContext) -> None:
    kb = [
        [types.KeyboardButton(text="Добавить канал"), types.KeyboardButton(text="Удалить канал")],
        [types.KeyboardButton(text="Мои каналы")],
    ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    await message.answer("Управление каналами", reply_markup=keyboard)


@chanel_handler_router.message(F.text == "Добавить канал")
async def add_channel_handler(message: Message, state: FSMContext) -> None:
    await message.answer("Перешлите пост из канала который вы хотите добавить в список каналов")
    await state.set_state(ManageChannelList.add_channel)


@chanel_handler_router.message(StateFilter(ManageChannelList.add_channel))
async def add_channel(message: Message, state: FSMContext) -> None:
    group_data = message.forward_from_chat
    id_channel = group_data.id
    name_channel = group_data.title
    ulr = group_data.linked_chat_id
    print(ulr)

    new_channel = TgChannel(
        name=name_channel, tg_id=id_channel, owner_id=message.from_user.id
    )
    await new_channel.create(session)
    print(name_channel, id_channel)
    await message.answer("Канал добавлен")
