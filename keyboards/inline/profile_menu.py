from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

profile_keyboard = InlineKeyboardMarkup(row_width=2,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(
                                                    text='Пополнить',
                                                    callback_data='up_balance'
                                                ),
                                                InlineKeyboardButton(
                                                    text='Просмотр заказов',
                                                    callback_data='view_orders'
                                                )
                                            ]
                                        ]
)