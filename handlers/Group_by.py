from aiogram import Router, types
from aiogram.filters.command import Command
from bot_config import bot
from datetime import timedelta
from profanity_check import predict_prob

group_router = Router()

BAD_WORDS = ("тупой", "дурак", "дебил")


@group_router.message(Command("ban", prefix="!"))
async def ban_user(message: types.Message):
    print(message.text)
    reply = message.reply_to_message
    print("Reply or not", reply)
    if reply:
        author = reply.from_user.id
        await bot.ban_chat_member(
            chat_id=message.chat.id,
            user_id=author,
            until_date=timedelta(seconds=90)
        )


@group_router.message()
async def filter_bad_words(message: types.Message):
    degree=predict_prob([message.text])
    if degree>0.6:
        await message.delete()
        await message.answer(
            f"Не ругайся {message.from_user.first_name}"
        )
        await bot.ban_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
