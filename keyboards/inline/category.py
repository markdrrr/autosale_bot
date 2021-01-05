from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api import category


async def get_inline_category():
    category_keyboard = InlineKeyboardMarkup(row_width=1)
    categories = await category.get_all_categories()
    for el in categories:
        buttom = InlineKeyboardButton(
            text=el.get('name'),
            callback_data=el.get('name')
        )
        category_keyboard.add(buttom)
    category_keyboard.add(InlineKeyboardButton(
                                                 text='Отмена',
                                                 callback_data='cancel'
                                             ))
    return category_keyboard
