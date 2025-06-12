# main.py
import asyncio
from aiogram import Bot, Dispatcher
from config import settings
from database.init_db import init_db
from handlers import start, listings, my_listings, all_listings


async def main():
    init_db()  # DB yaratish

    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()

    # Handlarni ro‘yxatdan o‘tkazish
    dp.include_routers(
        start.router,
        listings.router,
        my_listings.router,
        all_listings.router,
    )

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



