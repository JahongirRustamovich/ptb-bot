# handlers/my_listings.py
import os
from aiogram import Router, types, F
from aiogram.types import Message, FSInputFile
from database.listings import get_user_listings

router = Router()

@router.message(F.text == "E'lonlarim")
async def my_listings_handler(message: types.Message):
    listings = get_user_listings(message.from_user.id)

    if not listings:
        await message.answer("Sizda hali hech qanday "
                             "e'lon yo‘q.")
        return

    for listing in listings:
        (listing_id, location, price, rent_type, rooms,
         photo_path, description, created_at) = listing

        caption = (
            f"📍 Joylashuv: {location}\n"
            f"💰 Narx: {price} so'm\n"
            f"🏠 Tur: {rent_type}\n"
            f"🛏 Xonalar: {rooms}\n"
            f"🕒 E'lon qilingan: {created_at}\n"
            f"📝 Tavsif: {description}"
        )

        try:
            # `photo_path` bu yerda aslida `file_id`, shuning
            # uchun to'g'ridan-to'g'ri ishlatamiz
            await message.answer_photo(photo=photo_path,
                                       caption=caption)
        except Exception as e:
            await message.answer(f"{caption}\n\n⚠️ Rasmni "
                                 f"yuklab bo‘lmadi.\nXato: {e}")




