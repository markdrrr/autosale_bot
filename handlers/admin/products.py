from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery

from data.config import admins
from keyboards.inline.category import get_inline_category
from loader import dp
from states import NewProduct
from utils.db_api.sqlite.category import get_all_categories, get_category
from utils.db_api.sqlite.product import add_product


@dp.message_handler(Command('add_product'))
async def add_product_handler(message: types.Message):
    if str(message.from_user.id) in admins:
        categories = get_all_categories()
        if categories:
            markup = await get_inline_category()
            await message.answer(f'<b>Вы начали добавление товара</b>\n'
                                 f'Выберите категорию:',
                                 reply_markup=markup)
            await NewProduct.Category.set()
        else:
            await message.answer(f'<b>Категорий нет</b>\n'
                                 f'добавьте категорию командой\n'
                                 f'/add_category')


@dp.callback_query_handler(state=NewProduct, text='cancel')
async def cancel(cl: CallbackQuery, state: FSMContext):
    await cl.answer('Добавление отменено')
    await state.finish()
    await cl.message.delete()


@dp.callback_query_handler(state=NewProduct.Category)
async def add_product_step_1(cl: CallbackQuery, state: FSMContext):
    await cl.answer()
    bot = dp.bot
    await state.update_data(сategory=cl.data)
    await bot.send_message(cl.from_user.id, f'Пришлите название товара')
    await NewProduct.next()


@dp.message_handler(state=NewProduct.Name)
async def add_product_step_2(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(f'Пришлите описание товара')
    await NewProduct.next()


@dp.message_handler(state=NewProduct.Description)
async def add_product_step_3(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer(f'Пришлите цену товара')
    await NewProduct.next()


@dp.message_handler(state=NewProduct.Price)
async def add_product_step_4(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    data = await state.get_data()
    await message.answer(f'<b>Вы добавили товар в кат-рию:</b> {data.get("сategory")}\n'
                         f'<b>Название:</b> {data.get("name")}\n'
                         f'<b>Описание:</b> {data.get("description")}\n'
                         f'<b>Цена:</b> {data.get("price")}')
    await state.finish()
    id_category = get_category(name=data.get("сategory"))
    add_product(id_category[0], data.get("name"), data.get("description"), data.get("price"))
