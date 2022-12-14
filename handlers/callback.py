from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp

async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_1)
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
        reply_markup=markup
    )



async def quiz_3(call: types.CallbackQuery):
    question = "Сколько букв в русском алфавите?"
    answers = [
        "36",
        "33",
        "27",
        "29",
        "32"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="IZI",
        open_period=10,
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")