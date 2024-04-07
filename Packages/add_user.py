import Config
import asyncio
from Linux import *
from Mongo import *
from pyrogram import *
from pyrogram.types import *

@App.on_message(filters.command("add_user") & filters.user(Config.OWNER))
async def addUser(app: App, message: Message):
    if not message.reply_to_message:
        return await message.reply("**Syntax :** Reply To User To Add In Database.")
    user = message.reply_to_message.from_user
    if not await check_user(user.id):
        await add_user(user.id, user.first_name)
        return await message.reply(f"**Success ! Added User ID :** `{user.id}`")
    else:
        return await message.reply(f"**User ID Already Exists :** `{user.id}`")

@App.on_message(filters.user(Config.OWNER) & filters.command("resetacc"))
async def resetAccount(app: App, message: Message):
    if len(message.command) < 2:
        return await message.reply("**Syntax : /resetacc User ID**")
    check = message.command[1]
    user = await app.get_chat(check)
    await remove_user(user.id)
    sec = await message.reply("**Processing...**")
    datetime.datetime.now().timestamp()
    await asyncio.sleep(2)
    try:
        await sec.edit(f"**Success ! Reset User ID :** `{user.id}`")
    except:
        pass
