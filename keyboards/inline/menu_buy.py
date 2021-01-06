from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils.db_api.sqlite.category import get_all_categories
from utils.db_api.sqlite.product import get_all_products

menu_cd = CallbackData('show_menu', 'level', "category", 'item_id', 'count')
buy_item = CallbackData('buy', 'item_id', 'count')


def make_callback_data(level, category, item_id='0', count=0):
    return menu_cd.new(level=level, category=category, item_id=item_id, count=count)


async def categories_keyboard():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=1)
    categories = get_all_categories()
    for el in categories:
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           category=el[0])
        markup.insert(
            InlineKeyboardButton(text=el[1], callback_data=callback_data)
        )
    markup.row(
        InlineKeyboardButton(
            text='Отмена',
            callback_data='cancel'
        )
    )
    return markup


async def items_keyboard(category):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(row_width=1)
    items = get_all_products()
    for item in items:
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           category=category,
                                           item_id=item[0])
        markup.insert(
            InlineKeyboardButton(text=item[1], callback_data=callback_data)
        )
    markup.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1,
                                             category=category)
        )
    )
    markup.row(
        InlineKeyboardButton(
            text='Отмена',
            callback_data='cancel'
        )
    )
    return markup


def item_keyboard(category, item_id):
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup()
    for i in range(1, 6):
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           category=category,
                                           item_id=item_id,
                                           count=i)
        markup.insert(
            InlineKeyboardButton(
                text=f'{i}',
                callback_data=callback_data
            )
        )

    markup.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1,
                                             category=category)
        )
    )
    markup.row(
        InlineKeyboardButton(
            text='Отмена',
            callback_data='cancel'
        )
    )
    return markup


def confirm_keyboard(category, item_id, count):
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup()
    markup.insert(
        InlineKeyboardButton(
            text=f'Купить',
            callback_data=buy_item.new(item_id=item_id, count=count)
        )
    )
    markup.insert(
        InlineKeyboardButton(
            text='Назад',
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1,
                                             category=category,
                                             item_id=item_id, )
        )
    )
    markup.row(
        InlineKeyboardButton(
            text='Отмена',
            callback_data='cancel'
        )
    )
    return markup
