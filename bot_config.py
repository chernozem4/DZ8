from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
from os import getenv
from database.database import Database

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
database = Database("db_pizza.sqlite3.sqlite3")
debug = getenv("DEBUG", 0)
if not debug:
    print("Бот запускается на сервере")
    from aiogram.client.session.aiohttp import AiohttpSession
    session = AiohttpSession(proxy=getenv("PROXY"))
    bot = Bot(token=getenv("BOT_TOKEN"), session=session)
else:
    print("Бот запущен на компьютере")
    bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()
database = Database('db_pizza.sqlite3')