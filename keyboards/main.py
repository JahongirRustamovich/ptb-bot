# keyboards/main.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# main_menu (keyboards/main.py)
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="E'lon qo'shish")],
        [KeyboardButton(text="E'lonlarim")],
        [KeyboardButton(text="Barcha e'lonlar")],
    ],
    resize_keyboard=True
)



