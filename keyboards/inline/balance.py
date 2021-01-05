from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils.misc import Payment

separate_sms = CallbackData('separate_sms', 'qiwi_wallet', 'comment')
paid_callback = CallbackData('paid', 'data')


async def balance_inline(qiwi_wallet: str, payment: Payment):
    markup = InlineKeyboardMarkup(row_width=1,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(
                                              text='Перейти для оплаты',
                                              url=payment.link
                                          )],
                                  ])
    markup.insert(
        InlineKeyboardButton(
            text='Получить реквизиты в отдельных смс',
            callback_data=separate_sms.new(qiwi_wallet=qiwi_wallet, comment=payment.id)
        )
    )
    markup.insert(
        InlineKeyboardButton(
            text='Я пополнил',
            callback_data=paid_callback.new(data=payment.id)
        )
    )
    return markup
