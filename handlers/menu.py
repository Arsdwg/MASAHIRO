from aiogram import Router, F, types
from aiogram.types import FSInputFile
from aiogram.filters import Command


menu_router = Router()

@menu_router.message(Command("menu"))
async def get_menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[[
            types.KeyboardButton(text='Cуши'),
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

@menu_router.message(F.text.lower() == 'cуши')
async def sushi(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    shi = FSInputFile('image/image4.jpg')
    await message.answer_photo(shi, reply_markup=kb)

@menu_router.message(F.text.lower() == 'пицца')
async def sushi(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    shi = FSInputFile('image/image6.jpg')
    await message.answer_photo(shi, reply_markup=kb)

@menu_router.message(F.text.lower() == 'сеты')
async def sushi(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    shi = FSInputFile('image/image5.jpg')
    await message.answer_photo(shi, reply_markup=kb)

@menu_router.message(F.text.lower() == 'добавки')
async def sushi(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    shi = FSInputFile('image/image7.jpg')
    await message.answer_photo(shi, reply_markup=kb)

@menu_router.message(F.text.lower() == 'рамен')
async def sushi(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    shi = FSInputFile('image/image1.jpg')
    await message.answer_photo(shi, reply_markup=kb)

@menu_router.message(F.text.lower() == 'салаты')
async def sushi(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    shi = FSInputFile('image/image2.jpg')
    await message.answer_photo(shi, reply_markup=kb)
