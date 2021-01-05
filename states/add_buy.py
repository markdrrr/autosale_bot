from aiogram.dispatcher.filters.state import StatesGroup, State


class NewBuy(StatesGroup):
    Category = State()
    Product = State()
