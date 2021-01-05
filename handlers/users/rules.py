from aiogram import types

from loader import dp


@dp.message_handler(text='📜 Правила')
async def bot_start(message: types.Message):
    await message.answer("""
        Все правила изложены в этом ответе..
Ну по крайней мере должны были тут)
        """)
