from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery

from data.config import admins
from keyboards.inline.cancel import cancel_button
from loader import dp
from states import NewCategory
from utils.db_api.sqlite.category import add_category


@dp.message_handler(Command('add_category'))
async def add_product(message: types.Message):
    if str(message.from_user.id) in admins:
        await message.answer(f'<b>Вы начали добавление категории</b>\n'
                             f'Пришлите название',
                             reply_markup=cancel_button)
        await NewCategory.Name.set()


@dp.message_handler(state=NewCategory.Name)
async def add_product_step_1(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(f'Категория добавлена')
    data = await state.get_data()
    await state.finish()
    add_category(data.get('name'))


@dp.callback_query_handler(state=NewCategory, text='cancel')
async def cancel(cl: CallbackQuery, state: FSMContext):
    await cl.answer('Добавление отменено')
    await state.finish()
    await cl.message.delete()
