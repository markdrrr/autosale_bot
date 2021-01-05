from aiogram import types
from aiogram.types import CallbackQuery
from utils.db_api import order, product, staff
from keyboards.inline.profile_menu import profile_keyboard
from loader import dp, db
from utils.db_api.qiwi import get_payments_from_user


@dp.message_handler(text='Профиль')
async def bot_start(message: types.Message):
    user = message.from_user
    result = await db.select_user(id=user.id)
    count_order = await order.count_order(user_id=user.id)

    total_history_balance = 0
    payments = await get_payments_from_user(user_id=user.id)
    for payment in payments:
        total_history_balance += float(payment.get('sum'))
    await message.answer(f'<b>ИД:</b>  {user.id}\n'
                         f'<b>Никнейм:</b> @{user.username}\n'
                         f'<b>Текущий баланс:</b> {result.get("balance")}\n'
                         f'<b>Количество всех заказов:</b> {count_order}\n'
                         f'<b>Сумма всех пополнений:</b> {total_history_balance}\n',
                         reply_markup=profile_keyboard
                         )


# ответ на кнопку "Просмотр заказов"
@dp.callback_query_handler(text='view_orders')
async def view_orders(call: CallbackQuery):
    await call.answer()
    user = call.from_user
    orders = await order.select_orders_from_user(user_id=user.id)
    text = f'<b>Ваши заказы:</b>\n'
    for el in orders:
        item = await product.select_product(id=el.get("product_id"))
        item_staff_in_order = await order.get_staff_in_order(order_id=el.get('id'))
        text_staff = str()
        if item_staff_in_order:
            for i, st in enumerate(item_staff_in_order, start=1):
                item_staff = await staff.select_staff(id=st.get('staff_id'))
                text_staff += f'{i} {item_staff.get("staff")}\n'
        text += f'Заказ №{el.get("id")}\n' \
                f'Дата заказа: {el.get("data")}\n' \
                f'Товар: {item.get("name")}\n' \
                f'Содержание: {text_staff}\n' \
                f'Сумма покупки: {el.get("sum")}\n\n'
    await dp.bot.send_message(user.id, text)
