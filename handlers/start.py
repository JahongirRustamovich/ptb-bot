# handlers/start.py
from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards.main import main_menu

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Assalomu alaykum!\n\nKerakli bo‘limni tanlang:",
        reply_markup=main_menu
    )




