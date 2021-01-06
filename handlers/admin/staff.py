from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery

from data.config import admins
from keyboards.inline.products import get_inline_products
from loader import dp
from states import NewStaff
from utils.db_api.sqlite.product import get_all_products, select_product
from utils.db_api.sqlite.staff import add_staff


@dp.message_handler(Command('add_staff'))
async def add_staff_handler(message: types.Message):
    if str(message.from_user.id) in admins:
        products = get_all_products()
        if products:
            markup = await get_inline_products()
            await message.answer(f'<b>Вы начали добавление staff`a в товар</b>\n'
                                 f'Выберите товар:',
                                 reply_markup=markup)
            await NewStaff.Product_id.set()
        else:
            await message.answer(f'<b>Товаров нет</b>\n'
                                 f'добавьте товар командой\n'
                                 f'/add_product')


@dp.callback_query_handler(state=NewStaff, text='cancel')
async def cancel(cl: CallbackQuery, state: FSMContext):
    await cl.answer('Добавление отменено')
    await state.finish()
    await cl.message.delete()


@dp.callback_query_handler(state=NewStaff.Product_id)
async def add_staff_step_1(cl: CallbackQuery, state: FSMContext):
    await cl.answer()
    bot = dp.bot
    product_data = select_product(name=cl.data)
    await state.update_data(product_id=product_data[0])
    await bot.send_message(cl.from_user.id, f'Пришлите staff для товара')
    await NewStaff.next()


@dp.message_handler(state=NewStaff.Staff)
async def add_staff_step_2(message: types.Message, state: FSMContext):
    await state.update_data(staff=message.text)
    data = await state.get_data()
    product_data = select_product(id=data.get('product_id'))
    product_name = product_data[2]
    await message.answer(f'Вы добавили staff для товара\n'
                         f'{data.get("staff")}\n'
                         f'<b>{product_name}</b>')
    await state.finish()
    add_staff(data.get('product_id'), data.get('staff'))
