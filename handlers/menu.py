from aiogram import Router, F, types
from aiogram.types import FSInputFile
from aiogram.filters import Command


menu_router = Router()

@menu_router.message(Command("menu"))
async def get_menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[[
            types.KeyboardButton(text='Суши'),
            types.KeyboardButton(text='Пицца'),
            types.KeyboardButton(text='Рамен')
        ],
        [
            types.KeyboardButton(text='Сеты'),
            types.KeyboardButton(text='Добавки'),
            types.KeyboardButton(text='Салаты')
        ]
        ],
        resize_keyboard=True
    )
    await message.answer(f'Выберите тип еды:', reply_markup=kb)


food = ["пицца", "сеты", "добавки", "рамен", "салаты", 'суши']

@menu_router.message(F.text.lower().in_(food))
async def choose(message: types.Message):
    food = message.text.lower()
    kb = types.ReplyKeyboardRemove()
    if food == 'суши':
        shi = FSInputFile('image/image4.jpg')
        await message.answer_photo(shi, reply_markup=kb)
    elif food == 'пицца':
        shi = FSInputFile('image/image6.jpg')
        await message.answer_photo(shi, reply_markup=kb)
    elif food == 'рамен':
        shi = FSInputFile('image/image2.jpg')
        await message.answer_photo(shi, reply_markup=kb)
    elif food == 'сеты':
        shi = FSInputFile('image/image5.jpg')
        await message.answer_photo(shi, reply_markup=kb)
    elif food == 'добавки':
        shi = FSInputFile('image/image7.jpg')
        await message.answer_photo(shi, reply_markup=kb)
    elif food == 'салаты':
        shi = FSInputFile('image/image1.jpg')
        await message.answer_photo(shi, reply_markup=kb)