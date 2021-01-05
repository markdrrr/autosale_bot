from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from data.config import admins

from loader import dp


@dp.message_handler(Command('add_admin'))
async def bot_start(message: types.Message):
    await message.answer(f'Стать админом бота ?',
                             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                 [
                                     InlineKeyboardButton(
                                         text='Да !',
                                         callback_data='confirm_add_admin'
                                     )]
                                 ]
                             )
                         )


@dp.callback_query_handler(text='confirm_add_admin')
async def add_new_admin(call: CallbackQuery):
    await dp.bot.send_message(call.from_user.id, text=f'Вы теперь админ \n'
                                                      f'Можете попробовать команды\n'
                                                      f'/admin_help')
    admins.append(f'{call.from_user.id}')
