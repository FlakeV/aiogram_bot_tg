import logging

from aiogram import Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app import session
from models import User
from states.main_states import MainState
from states import EditAdminList


admin_handler_router = Router()





@admin_handler_router.message(Command("admin"))
async def admin_command_panel(message: Message, state: FSMContext) -> None:
    user = await User.get(session, message.from_user.id)
    if user.admin:
        logging.info(f"Admin {user} accessed admin panel")

        kb = [
            [types.KeyboardButton(text="/Admin_panel")],
            [types.KeyboardButton(text="/Admin_list")],
            [types.KeyboardButton(text="/Set_admin")],
            [types.KeyboardButton(text="/Delete_admin")],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
        await message.answer("Admin panel", reply_markup=keyboard)
        await state.set_state(MainState.admin)
    else:
        await message.answer("You are not admin")


@admin_handler_router.message(Command("Admin_list"), StateFilter(MainState.admin))
async def admin_list(message: Message, state: FSMContext) -> None:
    admin_list = await User.get_all_admins(session)
    await message.answer(f"Admin list: \n{'\n'.join([str(admin) for admin in admin_list])}")


@admin_handler_router.message(Command("Admin_panel"), StateFilter(MainState.admin))
async def admin_panel(message: Message) -> None:
    await message.answer("Admin panel")


@admin_handler_router.message(Command("Set_admin"), StateFilter(MainState.admin))
async def start_set_admin(message: Message, state: FSMContext) -> None:
    await message.answer("insert tg_id")
    await state.set_state(EditAdminList.insert_id)


@admin_handler_router.message(StateFilter(EditAdminList.add_admin))
async def set_admin(message: Message, state: FSMContext) -> None:
    try:
        new_admin_id = int(message.text)
    except ValueError:
        await message.answer("Invalid tg_id")
        return

    user_to_admin = await User.get(session, new_admin_id)
    if user_to_admin:
        logging.info(f"Admin {message.from_user.id} set admin {message.text}")
        await User.set_admin_to_user(session, user_to_admin, True)
        await message.answer("Admin added")
        await state.clear()
    else:
        await message.answer("User not found")


@admin_handler_router.message(Command("Delete_admin"), StateFilter(MainState.admin))
async def start_delete_admin(message: Message, state: FSMContext) -> None:
    await message.answer("insert tg_id")
    await state.set_state(EditAdminList.delete_admin)


@admin_handler_router.message(StateFilter(EditAdminList.delete_admin))
async def delete_admin(message: Message, state: FSMContext) -> None:
    try:
        new_admin_id = int(message.text)
    except ValueError:
        await message.answer("Invalid tg_id")
        return

    user_to_admin = await User.get(session, new_admin_id)
    if user_to_admin:
        logging.info(f"Admin {message.from_user.id} deleted admin {message.text}")
        await User.set_admin_status_to_user(session, user_to_admin, False)
        await message.answer("Admin deleted")
        await state.clear()
    else:
        await message.answer("User not found")
