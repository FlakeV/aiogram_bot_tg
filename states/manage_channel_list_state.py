from aiogram.fsm.state import StatesGroup, State

class ManageChannelList(StatesGroup):
    add_channel = State()
    delete_channel = State()