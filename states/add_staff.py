from aiogram.dispatcher.filters.state import StatesGroup, State


class NewStaff(StatesGroup):
    Product_id = State()
    Staff = State()
