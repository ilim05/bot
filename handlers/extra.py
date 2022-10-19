from aiogram import types, Dispatcher
from config import bot, dp
import random

async def echo(message: types.Message):
    if message.text.isdigit() == True:
        b = int(message.text)
        await bot.send_message(message.chat.id, b*b)
    elif message.reply_to_message == "!pin":
        await bot.pin_chat_message(message.chat.id, message.message_id)
    elif message.text.startswith("game"):
        c = ['⚽', '🏀', '🎯', '🎰']
        b = await bot.send_dice(message.chat.id, emoji=random.choice(c))
    else:
        await bot.send_message(message.from_user.id, message.text)

def registr_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)