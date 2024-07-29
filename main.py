import asyncio
import logging
from aiogram import Bot, Dispatcher
from bot_config import bot, dp, database
from handlers.start import start_router
from handlers.dishes import dishes_router
from handlers.review_dialog import review_router
from handlers.myinfo import my_info_router
from handlers.menu import menu_router
from handlers.Group_by import group_router

async def on_startup(bot: Bot):
    database.create_tables()


async def main():
    # запуск бота
    dp.include_router(start_router)
    dp.include_router(review_router)
    dp.include_router(my_info_router)
    dp.include_router(dishes_router)
    dp.include_router(menu_router)
    dp.include_router(group_router)
    dp.startup.register(on_startup)
    #  Запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


