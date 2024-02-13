from aiogram.fsm.state import StatesGroup, State


class EditAdminList(StatesGroup):
    add_admin = State()
    delete_admin = State()
