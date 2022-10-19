from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, storage
from keyboards.client_kb import FSM_Direction, FSM_Group, FSM_Submit, FSM_Cancel
import random
a = range(1,1001)
b = random.choice(a)
c = [0]
class FSMAdmin(StatesGroup):
    mentor_id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.mentor_id.set()
        try:
            if c.count(b) == 0:
                await message.answer(f"tvoi id {b}")
        except:
            b
        reply_markup = FSM_Cancel
    else:
        await message.answer("pishi v lichku ppo bratski")

async def load_mentor_id(message: types.Message, state: FSMContext):
    async with state.proxy() as storage:
        storage['id'] = message.from_user.id
        storage['username'] = f"@{message.from_user.username}"
        storage['mentor_id'] = b
    await FSMAdmin.next()
    await message.answer("Kak zvat?")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as storage:
        storage['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Kakoe napravlenie?', reply_markup=FSM_Direction)

async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as storage:
        storage['direction'] = message.text
    await FSMAdmin.next()
    await message.answer('Skok let?')

async def load_age(message: types.Message, state: FSMContext):
    try:
        if int(message.text) < 16 or int(message.text) > 50:
            await message.answer('dostup zapreshen!!!')
        else:
            async with state.proxy() as storage:
                storage['age'] = int(message.text)
            await FSMAdmin.next()
            await message.answer('S kakoi gruppy?', reply_markup=FSM_Group)
    except:
        await message.answer('pishi tsyvry')

async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as storage:
        storage['group'] = int(message.text)
        await bot.send_message(message.from_user.id, storage['id'],
                               caption=f'{storage["name"]}, {storage["direction"]}'
                               f'{storage["age"]}, {storage["group"]}')

    await FSMAdmin.next()
    await message.answer('Vse norm?', reply_markup=FSM_Submit)

async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "Da":
        await state.finish()
        await message.answer('registratsia zavershena')
    if message.text.lower() == 'Net':
        await state.finish()
        await message.answer('otmeneno!')

async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('otmeneno!')

def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True),
                                state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(fsm_start, Text(equals='reg', ignore_case=True))
    dp.register_message_handler(load_mentor_id, state=FSMAdmin.mentor_id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)