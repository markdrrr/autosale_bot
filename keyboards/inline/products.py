from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.sqlite.product import get_all_products


async def get_inline_products():
    products_keyboard = InlineKeyboardMarkup(row_width=1)
    products = get_all_products()
    for el in products:
        buttom = InlineKeyboardButton(
            text=el[1],
            callback_data=el[1]
        )
        products_keyboard.add(buttom)
    products_keyboard.add(InlineKeyboardButton(
        text='Отмена',
        callback_data='cancel'
    ))
    return products_keyboard
