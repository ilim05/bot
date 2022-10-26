from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.bot_db import sql_command_all, sql_command_delete
from aiogram import types, Dispatcher
from config import bot, dp, Admin
from aiogram.dispatcher.filters import Text
async def delete_storage(message: types.Message):
    if not message.from_user.id in Admin:
        await message.answer(f"ty mne ne boss ")
    else:
        users = await sql_command_all()
        for user in users:
            await bot.send_message(message.from_user.id, f"{user[2]},{user[3]},"
                                                         f"{user[4]},{user[5]}\n\n{user[1]}",
                                   reply_markup=InlineKeyboardMarkup().add(
                                       InlineKeyboardButton(f"Delete {user[2]}",
                                                            callback_data=f"delete {user[0]}")
                                   ))

async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace('delete ', ''))
    await call.answer(text="udaleno iz bd", show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(delete_storage, commands=['del'])
    dp.register_message_handler(delete_storage, Text(equals='del', ignore_case=True))
    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith('delete '))