from aiogram.fsm.state import StatesGroup, State


class MainState(StatesGroup):
    admin = State()
    add_chanel = State()
    chanel_list = State()
