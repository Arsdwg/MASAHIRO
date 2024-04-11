import asyncio
import logging
from config import bot, dp, my_menu
from handlers.echo import echo_router
from handlers.start import start_router
from handlers.menu import menu_router
from handlers.help import help_router
from handlers.survey import survey_router

async def main():
    await my_menu()
# роутеры
    dp.include_router(start_router)
    dp.include_router(survey_router)
# команды
    dp.include_router(menu_router)
    dp.include_router(help_router)
# эхо
    dp.include_router(echo_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())