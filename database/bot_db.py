import sqlite3
import random
from config import bot

def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("bd podkluchena")

    db.execute("CREATE TABLE IF NOT EXISTS anketa"
               "(id INTEGER PRIMARY KEY, username TEXT, name TEXT,"
               "direction TEXT, age INTEGER, groupa INTEGER)")
    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as storage:
        cursor.execute("INSERT INTO anketa VALUES (?,?,?,?,?,?)", tuple(storage.values()))
        db.commit()

async def sql_command_random(message):
    results = cursor.execute("SELECT * FROM anketa").fatchall()
    random_user = random.choice(results)
    await bot.send_message(message.from_user.id, f"{random_user[2]},{random_user[3]},"
                           f"{random_user[4]},{random_user[5]}\n\n{random_user[1]}")


async def sql_command_all():
    return cursor.execute("SELECT * FROM anketa").fetchall()

async def sql_command_delete(id):
    cursor.execute("DELETE FROM anketa WHERE id = ?", (id, ))
    db.commit()