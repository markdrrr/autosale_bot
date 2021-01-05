import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menu import menu
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!',
                         reply_markup=menu
                         )
    user = message.from_user
    try:
        await db.add_user(user.id, user.username)
        await message.answer(f'Вы зарегестрированны')
    except asyncpg.exceptions.UniqueViolationError:
        await message.answer(f'Вы уже были зарегестрированны')


@dp.message_handler(text='О боте🔒')
async def about(message: types.Message):
    await message.answer("""
        автор бота @miduzzza
<a href="https://github.com/markdrrr/autosale_bot">Исходник бота на гитхаб</a>
        """)