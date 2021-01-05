from aiogram.dispatcher.filters.state import StatesGroup, State


class NewProduct(StatesGroup):
    Category = State()
    Name = State()
    Description = State()
    Price = State()
