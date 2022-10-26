import asyncio
import logging
from aiogram.utils import executor
from config import bot, dp
from handlers import client, callback, extra, fsm_anketa, admin, notifications
from database.bot_db import sql_create

async def on_startup(_):
    asyncio.create_task(notifications.scheduler())
    sql_create()

admin.register_handlers_admin(dp)
fsm_anketa.register_handlers_fsm_anketa(dp)
client.register_handlers_client(dp)
notifications.register_handlers_notification(dp)
callback.register_handlers_callback(dp)
extra.registr_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

