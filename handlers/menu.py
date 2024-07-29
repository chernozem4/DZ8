from bot_config import bot,dp
from aiogram import types,Router,F
from aiogram.filters import Command
import random
from aiogram.types import FSInputFile
from bot_config import database
menu_router = Router()


@menu_router.message(Command('menu'))
async def menu(message: types.Message):
    kb=types.InlineKeyboardMarkup(
        inline_keyboard=[

            [types.InlineKeyboardButton(text='Пепперони', callback_data='Pepperoni')],
            [types.InlineKeyboardButton(text='99 сыров', callback_data='99_cheese')],
            [types.InlineKeyboardButton(text='Болоньезе', callback_data='Boloneze')],
            [types.InlineKeyboardButton(text='4 сезона', callback_data='4_season')],
            [types.InlineKeyboardButton(text='Цезарь', callback_data='Cesar')],
            [types.InlineKeyboardButton(text='Тайская', callback_data='Tay_pizza')],
            [types.InlineKeyboardButton(text='Мексикано', callback_data='Mexicano')],
        ]
    )
    await message.answer('наш ассортимент на данный момент', reply_markup=kb)


signal=('Pepproni','99_cheese', 'Boloneze', '4_season', 'Cesar', 'Tay_pizza', 'Mexicano')

@menu_router.callback_query(lambda call:call.data in signal)
async def dishes(call:types.CallbackQuery):
    query='''
    SELECT * FROM dishes JOIN categories ON dishes.category_id = categories.id WHERE categories.name = ?'''

    data=database.fetch(
        query=query,
        params=(call.data,)
    )
    for i in data:
        photo = FSInputFile(i[3])
        await call.message.answer_photo(photo=photo,caption=f'name: {i[1]}\n'
                                                            f'price: {i[2]}')