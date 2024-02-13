from typing import List, AnyStr

from aiogram import types


class ReplyKeyboardBuilder:
    @staticmethod
    async def build(
        keyboard_buttons: List[List[AnyStr]], one_time_keyboard: bool = False, user_is_admin: bool = False
    ) -> types.ReplyKeyboardMarkup:
        kb = []
        for row in keyboard_buttons:
            kb.append([])
            for button in row:
                button = types.KeyboardButton(text=button)
                kb[-1].append(button)

        if user_is_admin:
            kb.append([types.KeyboardButton(text="/admin")])
        return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=one_time_keyboard)
