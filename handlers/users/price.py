from aiogram import types

from loader import dp
from utils.db_api.sqlite.category import get_all_categories
from utils.db_api.sqlite.product import get_products_from_category
from utils.db_api.sqlite.staff import get_count


@dp.message_handler(text='Прайс')
async def bot_start(message: types.Message):
    categories = get_all_categories()
    text = str()
    for categ in categories:
        text += f'➖➖➖ {categ[1]} ➖➖➖\n'
        products = get_products_from_category(categ[0])
        for el in products:
            count = get_count(product_id=categ[0], status=0)
            text += f'<b>{el[2]}</b> в наличии: {count[0]}шт. цена: {el[4]}р/шт.\n'
    if text:
        await message.answer(f'{text}')
    else:
        await message.answer(f'Прайслист пуст')
