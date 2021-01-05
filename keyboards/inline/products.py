from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api import product


async def get_inline_products():
    products_keyboard = InlineKeyboardMarkup(row_width=1)
    products = await product.get_all_products()
    for el in products:
        buttom = InlineKeyboardButton(
            text=el.get('name'),
            callback_data=el.get('name')
        )
        products_keyboard.add(buttom)
    products_keyboard.add(InlineKeyboardButton(
                                                 text='Отмена',
                                                 callback_data='cancel'
                                             ))
    return products_keyboard
