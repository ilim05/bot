from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton("start"), KeyboardButton("quiz")).add( KeyboardButton("mem"), KeyboardButton("reg")).add(KeyboardButton("game"))
FSM_Direction = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton("BackEnd"), KeyboardButton("FrontEnd"), KeyboardButton("Android Developer"),
      KeyboardButton("IOS Developer"), KeyboardButton("Basics of Programming"), KeyboardButton("Manager of Projects")).add(KeyboardButton("CANCEL"))

FSM_Group = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('1'), KeyboardButton('2'), KeyboardButton('3')).add(KeyboardButton("CANCEL"))

FSM_Submit = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton("Da"), KeyboardButton("Net")).add(KeyboardButton("CANCEL"))

FSM_Cancel =ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton("CANCEL"))
