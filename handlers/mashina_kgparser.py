from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from my_parser.mashina_kg import HouseParser

house_router = Router()


@house_router.message(Command("flats"))
async def house_links(message: types.Message):
    parser = HouseParser()
    parser.get_page()
    links = parser.get_house_links()
    if links:
        for link in links:
            await message.answer(link, parse_mode=ParseMode.HTML)
    else:
        await message.answer("нету ссылки")