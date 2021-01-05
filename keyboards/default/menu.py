from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Купить'),
            KeyboardButton(text='Прайс')
        ],
        [
            KeyboardButton(text='Профиль'),
        ],
        [
            KeyboardButton(text='📜 Правила'),
            KeyboardButton(text='🆘 Помощь'),
            KeyboardButton(text='О боте🔒')
        ]
    ],
    resize_keyboard=True
)
