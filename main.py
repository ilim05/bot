from aiogram import types, Dispatcher
from aiogram.utils import executor
from config import bot, dp
from handlers import client, callback, extra, fsm_anketa

fsm_anketa.register_handlers_fsm_anketa(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
extra.registr_handlers_extra(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

