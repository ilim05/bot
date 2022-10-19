from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

FSM_Direction = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton("BackEnd"), KeyboardButton("FrontEnd"), KeyboardButton("Android Developer"),
      KeyboardButton("IOS Developer"), KeyboardButton("Basics of Programming"), KeyboardButton("Manager of Projects"))

FSM_Group = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('1'), KeyboardButton('2'), KeyboardButton('3'))

FSM_Submit = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton("Da"), KeyboardButton("Net"))

FSM_Cancel =ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton("CANCEL"))