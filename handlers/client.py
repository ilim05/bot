from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import random
from aiogram.dispatcher.filters import Text
from keyboards.client_kb import start_markup
from database.bot_db import sql_command_random
from parser.anime import parser

async def start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Салам хозяин {message.from_user.first_name}!",
                           reply_markup=start_markup)

async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)
    question = "Кто является лучшим футболистом?"
    answers = [
        'Месси',
        'Роналду',
        'Роналдиньо',
        'Марадонна',
        'Пеле'
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="IZI",
        open_period=10,
        reply_markup=markup
    )

async def sendphoto(msg):
    a = ['mems/mem1/mem1.jpg', 'mems/mem2/mem2.jpg', 'mems/mem3/mem3.jpg', 'mems/mem4/mem4.jpg','mems/mem5/mem5.jpg']
    photo = open(random.choice(a), 'rb')
    await bot.send_photo(chat_id=msg.from_user.id, photo=photo)

async def get_random_user(message: types.Message):
    await sql_command_random(message)

async def parser_film(message: types.Message):
    items = parser()
    for item in items:
        await message.answer(
            f"{item['link']}\n\n"
            f"{item['title']}\n"
            f"#Y{item['year']}\n"
            f"#{item['country']}\n"
            f"#{item['genre']}\n"
        )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(quiz_1, Text(equals='quiz', ignore_case=True))
    dp.register_message_handler(sendphoto, commands=['mem'])
    dp.register_message_handler(sendphoto, Text(equals='mem', ignore_case=True))
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(start, Text(equals='start', ignore_case=True))
    dp.register_message_handler(sql_command_random, commands=['get'])
    dp.register_message_handler(sql_command_random, Text(equals='get', ignore_case=True))
    dp.register_message_handler(parser_film, commands=['film'])