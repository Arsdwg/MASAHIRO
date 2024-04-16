from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from pathlib import Path
from database.major import DataBase



load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()
database = DataBase(
    Path(__file__).parent / 'data.db'
)

async def my_menu():
    await bot.set_my_commands([
        types.BotCommand(command='start', description='Начать'),
        types.BotCommand(command='menu', description='Меню'),
        types.BotCommand(command='help', description='Помощь')
    ])
