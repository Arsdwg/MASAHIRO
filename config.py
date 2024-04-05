from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()

async def my_menu():
    await bot.set_my_commands([
        types.BotCommand(command='start', description='Начать'),
        types.BotCommand(command='menu', description='Меню'),
        types.BotCommand(command='help', description='Помощь')
    ])
