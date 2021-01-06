from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.profile_menu import profile_keyboard
from loader import dp
from utils.db_api.sqlite.order import count_orders, select_orders_from_user, get_staff_in_order
from utils.db_api.sqlite.product import select_product
from utils.db_api.sqlite.qiwi import get_payments_from_user
from utils.db_api.sqlite.staff import select_staff
from utils.db_api.sqlite.user import select_user


@dp.message_handler(text='Профиль')
async def bot_start(message: types.Message):
    user = message.from_user
    result = select_user(id=user.id)
    count_order = count_orders(user_id=user.id)

    total_history_balance = 0
    payments = get_payments_from_user(user_id=user.id)
    for payment in payments:
        total_history_balance += float(payment[3])
    await message.answer(f'<b>ИД:</b>  {result[0]}\n'
                         f'<b>Никнейм:</b> @{result[1]}\n'
                         f'<b>Текущий баланс:</b> {result[2]}\n'
                         f'<b>Количество всех заказов:</b> {count_order[0]}\n'
                         f'<b>Сумма всех пополнений:</b> {total_history_balance}\n',
                         reply_markup=profile_keyboard
                         )


# ответ на кнопку "Просмотр заказов"
@dp.callback_query_handler(text='view_orders')
async def view_orders(call: CallbackQuery):
    await call.answer()
    user = call.from_user
    orders = select_orders_from_user(user_id=user.id)
    text = f'<b>Ваши заказы:</b>\n'
    for el in orders:
        item = select_product(id=el[2])
        item_staff_in_order = get_staff_in_order(order_id=el[0])
        text_staff = str()
        if item_staff_in_order:
            for i, st in enumerate(item_staff_in_order, start=1):
                item_staff = select_staff(id=st[2])
                text_staff += f'{i} {item_staff[2]}\n'
        text += f'Заказ №{el[0]}\n' \
                f'Дата заказа: {el[3]}\n' \
                f'Товар: {item[2]}\n' \
                f'Содержание: {text_staff}\n' \
                f'Сумма покупки: {el[4]}\n\n'
    await dp.bot.send_message(user.id, text)
