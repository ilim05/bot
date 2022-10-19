from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
try:
    if a.count(int(message.text)) == 0:
        async with state.proxy() as storage:
            storage['id'] = message.from_user.id
            storage['username'] = f"@{message.from_user.username}"
            storage['mentor_id'] = int(message.text)
            a.append(int(message.text))
            await FSMAdmin.next()
            await message.answer('Kak zvat?')
except:
    await message.answer('id zanyat poprobui drugoi id!!!')