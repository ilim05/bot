import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot

async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer("Ok")

async def aleeee():
    await bot.send_message(chat_id=chat_id, text='vyshla novaia seriya tvoego seriala')

async def scheduler():
    aioschedule.every().monday.at('18:00').do(aleeee)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'napomni' in word.text.lower())

