from utils import ReplyKeyboardBuilder

BUTTONS = [
    ["Забронировать место для рекламы", "Мои брони"],
    ["Мои каналы", "Мой профиль"],
]


async def main_keyboard(one_time_keyboard: bool = False, admin: bool = False):
    return await ReplyKeyboardBuilder.build(
        keyboard_buttons=BUTTONS, one_time_keyboard=one_time_keyboard, user_is_admin=admin
    )
