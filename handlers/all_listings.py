# handlers/all_listings.py
from aiogram import Router, F
from aiogram.types import Message
from database.listings import get_all_listings
from keyboards.main import main_menu  # tugmalar uchun

router = Router()

@router.message(F.text == "📋 Barcha e'lonlar")
async def all_listings_handler(message: Message):
    listings = get_all_listings()

    if not listings:
        await message.answer("❌ Hozircha "
                             "e'lonlar mavjud emas.")
        return

    for listing in listings:
        text = (
            f"📍 Manzil: {listing['location']}\n"
            f"💰 Narx: {listing['price']} so'm\n"
            f"🕒 Tur: {listing['rent_type']}\n"
            f"🛏 Xonalar: {listing['rooms']}\n"
            f"📝 Tavsif: {listing['description']}"
        )
        photo_id = listing.get("photo")

        if photo_id:
            try:
                await message.answer_photo(photo=photo_id,
                                           caption=text)
            except Exception as e:
                print(f"⚠️ Rasm yuklanmadi: {e}")
                await message.answer(text)
        else:
            await message.answer(text)



