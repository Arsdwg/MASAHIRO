from aiogram import types

def start_keyboard():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Наш сайт', url="https://masahiro.kg"),
                types.InlineKeyboardButton(text='Instagram', url="https://www.instagram.com/masahiro.kg")
            ],
            [
                types.InlineKeyboardButton(text='Контакты', callback_data='contact'),
                types.InlineKeyboardButton(text='Пожелания', callback_data='wish')
            ],
            [
                types.InlineKeyboardButton(text='Оставить отзыв', callback_data='survey')
            ]
        ]
    )
    return kb
