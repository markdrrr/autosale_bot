from aiogram import types
from loader import dp
from utils.db_api import product, category, staff


@dp.message_handler(text='Прайс')
async def bot_start(message: types.Message):
    categories = await category.get_all_categories()
    text = str()
    for categ in categories:
        text += f'➖➖➖ {categ.get("name")} ➖➖➖\n'
        products = await product.get_products_from_category(categ.get('id'))
        for el in products:
            count = await staff.get_count(product_id=categ.get('id'), status=0)
            text += f'<b>{el.get("name")}</b> в наличии: {count}шт. цена: {el.get("price")}р/шт.\n'
    if text:
        await message.answer(f'{text}')
    else:
        await message.answer(f'Прайслист пуст')
