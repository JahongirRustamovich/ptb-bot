# handlers/listings.py
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message, CallbackQuery
from db.listing import add_listing, get_user_listings, delete_listing
from db.user import get_user_id
from states.listing_states import ListingStates

router = Router()


@router.message(F.text.lower() == "e'lon qo'shish")
async def start_listing(message: Message, state: FSMContext):
    await message.answer("📍 Qayerda joylashgan? (Manzil)")
    await state.set_state(ListingStates.location)



@router.message(ListingStates.location)
async def enter_price(message: Message, state: FSMContext):
    await state.update_data(location=message.text)
    await message.answer("💰 Narxi qancha? (faqat son)")
    await state.set_state(ListingStates.price)


@router.message(ListingStates.price)
async def enter_rent_type(message: Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer("Iltimos, narxni faqat "
                                    "son bilan kiriting.")
    await state.update_data(price=int(message.text))
    await message.answer("🕒 Ijaraning turi: kunlik yoki oylik?")
    await state.set_state(ListingStates.rent_type)


@router.message(ListingStates.rent_type)
async def enter_rooms(message: Message, state: FSMContext):
    await state.update_data(rent_type=message.text)
    await message.answer("🛏 Necha xonali?")
    await state.set_state(ListingStates.rooms)


@router.message(ListingStates.rooms)
async def enter_photo(message: Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer("Iltimos, xonalar "
                                    "sonini faqat raqamda yozing.")
    await state.update_data(rooms=int(message.text))
    await message.answer("📸 Iltimos, uyning fotosuratini yuboring.")
    await state.set_state(ListingStates.photo)


@router.message(ListingStates.photo, F.photo)
async def enter_description(message: Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id  # eng sifatlisini olamiz
    await state.update_data(photo=photo_file_id)
    await message.answer("📝 Qo‘shimcha ma’lumot yoki ta’rif kiriting.")
    await state.set_state(ListingStates.description)


@router.message(ListingStates.description)
async def confirm_listing(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    data = await state.get_data()

    caption = (
        f"📍 Manzil: {data['location']}\n"
        f"💰 Narx: {data['price']} so'm\n"
        f"🕒 Tur: {data['rent_type']}\n"
        f"🛏 Xonalar: {data['rooms']}\n"
        f"📝 Ta’rif: {data['description']}"
    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Tasdiqlash",
                              callback_data="confirm_listing")],
        [InlineKeyboardButton(text="❌ Bekor qilish",
                              callback_data="cancel_listing")]
    ])

    await message.bot.send_photo(chat_id=message.chat.id,
                                 photo=data['photo'], caption=caption,
                                 reply_markup=markup)
    await state.set_state(ListingStates.confirm)


@router.callback_query(F.data == "confirm_listing")
async def save_listing(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = get_user_id(callback.from_user.id)

    add_listing(
        user_id=user_id,
        location=data['location'],
        price=data['price'],
        rent_type=data['rent_type'],
        rooms=data['rooms'],
        photo=data['photo'],
        description=data['description']
    )

    await callback.message.answer("✅ E'lon muvaffaqiyatli qo‘shildi.")
    await state.clear()


@router.callback_query(F.data == "cancel_listing")
async def cancel_listing(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("❌ E'lon bekor qilindi.")
    await state.clear()




