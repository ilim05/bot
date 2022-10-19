from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import random
from aiogram.dispatcher.filters import Text

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

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(quiz_1, Text(equals='quiz', ignore_case=True))
    dp.register_message_handler(sendphoto, commands=['mem'])
    dp.register_message_handler(sendphoto, Text(equals='mem', ignore_case=True))