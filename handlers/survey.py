from aiogram import Router, F, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


survey_router = Router()

class BookSurvey(StatesGroup):
    name = State()
    age = State()
    star = State()
    capt = State()


@survey_router.callback_query(F.data == 'survey')
async def get_survey(cb: types.CallbackQuery, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    await cb.answer()
    await state.set_state(BookSurvey.name)
    await cb.message.answer('Как вас зовут?', reply_markup=kb)

@survey_router.message(BookSurvey.name)
async def name(message: types.Message, state: FSMContext):
    await state.set_state(BookSurvey.age)
    await state.update_data(name=message.text)
    await message.answer(f'Сколько вам лет, {message.text}?')

@survey_router.message(BookSurvey.age)
async def age(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='⭐️'),
                types.KeyboardButton(text='⭐️⭐'),
                types.KeyboardButton(text='⭐️⭐⭐')
            ],
            [
                types.KeyboardButton(text='⭐️⭐⭐⭐'),
                types.KeyboardButton(text='⭐️⭐⭐⭐⭐')
            ]],
        resize_keyboard=True
    )
    age = message.text
    if int(age) < 10 or int(age) > 100:
        await message.answer('Вы слишком малы или мертвы чтобы оставить отзыв.')
        return
    await state.update_data(age=age)
    await state.set_state(BookSurvey.star)
    await message.answer('Поставьте нам оценку:', reply_markup=kb)

@survey_router.message(BookSurvey.star)
async def star(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    await state.set_state(BookSurvey.capt)
    await state.update_data(star=message.text)
    await message.answer('Напишите что вам понравилось/не понравилось', reply_markup=kb)

@survey_router.message(BookSurvey.capt)
async def capt(message: types.Message, state: FSMContext):
    await state.update_data(capt=message.text)
    await message.answer('Мы отправили ваш отзыв!')
    await state.clear()
