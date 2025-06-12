# states/listing_states.py
from aiogram.fsm.state import State, StatesGroup

class ListingStates(StatesGroup):
    location = State()
    price = State()
    rent_type = State()
    rooms = State()
    photo = State()
    description = State()
    confirm = State()





