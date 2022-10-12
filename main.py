from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
import random

@dp.message_handler(commands=['quiz'])
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

@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    question = "Сколько золотых мячей выиграл Месси?"
    answers = [
        "7",
        "5",
        "3",
        "1",
        "0"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="IZI",
        open_period=10,
    )
@dp.message_handler(commands=['mem'])
async def sendphoto(msg):
        a = ['mems/mem1/mem1.jpg', 'mems/mem2/mem2.jpg', 'mems/mem3/mem3.jpg', 'mems/mem4/mem4.jpg', 'mems/mem5/mem5.jpg']
        photo = open(random.choice(a), 'rb')
        await bot.send_photo(chat_id=msg.from_user.id, photo=photo)

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit() == True:
        b = int(message.text)
        await bot.send_message(message.chat.id, b*b)
    else:
        await bot.send_message(message.from_user.id, message.text)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)