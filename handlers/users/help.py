from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.config import admins
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку'
    ]
    await message.answer('\n'.join(text))


@dp.message_handler(text='🆘 Помощь')
async def bot_help_buy(message: types.Message):
    await message.answer("""
            Вся информация о помощи 
в этом разделе...
    """)


@dp.message_handler(Command('admin_help'))
async def bot_help_buy(message: types.Message):
    if str(message.from_user.id) in admins:
        await message.answer("""
                Команды для админа
Добавить категорию /add_category
Добавить товар /add_product
Добавить staff для товара /add_staff
        """)
