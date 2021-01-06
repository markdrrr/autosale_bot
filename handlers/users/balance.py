from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hcode

from data import config
from keyboards.inline.balance import balance_inline, separate_sms, paid_callback
from loader import dp
from utils.db_api.sqlite.qiwi import add_payment, update_payment, select_payment
from utils.db_api.sqlite.user import add_balance
from utils.misc import Payment, NoPaymentFound


@dp.callback_query_handler(text='up_balance')
async def up_balance(call: CallbackQuery):
    payment = Payment(call.from_user.id)
    await payment.create()
    add_payment(payment.id, call.from_user.id, 0, 'qiwi')
    markup = await balance_inline(config.WALLET_QIWI, payment)
    text = 'Для пополнения баланса, переведите денежные средства на счет\n' \
           f'QIWI: <b>{config.WALLET_QIWI}</b>\n' \
           f'C комментарием: <b>{hcode(payment.id)}</b>\n\n' \
           f'<b>Пополняя счет, вы автоматически принимаете наши правила!</b>\n\n' \
           f'После пополнения баланса нажмите на кнопку <b>"Я пополнил баланс"</b>'
    await call.message.edit_text(text)
    await call.message.edit_reply_markup(markup)


@dp.callback_query_handler(separate_sms.filter())
async def separate_sms_answer(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    bot = dp.bot
    await bot.send_message(call.from_user.id, callback_data.get('qiwi_wallet'))
    await bot.send_message(call.from_user.id, callback_data.get('comment'))


@dp.callback_query_handler(text='text', state='qiwi')
async def cancel_payment(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text('Отменено')
    await state.finish()


@dp.callback_query_handler(paid_callback.filter())
async def cancel_payment(call: CallbackQuery, callback_data: dict):
    payment_id = callback_data.get('data')
    amount = 0
    try:
        amount = Payment.check_payment(payment_id)
    except NoPaymentFound:
        await call.message.answer('Транзакция не найдена')
        return
    else:
        # проверяем есть ли такой плетж уже в бд
        old_payment = select_payment(sum=amount, key=payment_id)
        if old_payment is None:
            # обновляем сумму пополнения в бд
            update_payment(amount=amount, key=payment_id)
            # обновляем баланс юзера
            add_balance(user_id=call.from_user.id, value=amount)
            await call.message.answer(f'Баланс успешно пополнен на {amount}')
            await call.message.delete_reply_markup()
            await call.message.delete()
