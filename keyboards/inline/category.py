from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.sqlite.category import get_all_categories


async def get_inline_category():
    category_keyboard = InlineKeyboardMarkup(row_width=1)
    categories = get_all_categories()
    for el in categories:
        buttom = InlineKeyboardButton(
            text=el[1],
            callback_data=el[1]
        )
        category_keyboard.add(buttom)
    category_keyboard.add(InlineKeyboardButton(
        text='Отмена',
        callback_data='cancel'
    ))
    return category_keyboard
