"""
import Config
import asyncio
from pyrogram import filters
from Linux import App as Soumo
from pyrogram.types import Message
from pyrogram import Client as PyroGram
from pyrogram.enums import ChatType
from Packages import ALL_MODULES
from importlib import import_module
import importlib

@Soumo.on_message(filters.command("clone", ["$", "!", ".", "/", "?"]))
async def cloneFuncs(Soumo:Soumo, message:Message):
    if message.chat.type != ChatType.PRIVATE:
        return await message.reply("**ᴋɪɴᴅʟʏ ᴜsᴇ ɪɴ ᴘʀɪᴠᴀᴛᴇ !**")
    Cexc = await message.reply("**» Sᴛᴀʀᴛɪɴɢ ᴘʀᴏᴄᴄᴇss ᴋɪɴᴅʟʏ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...**")
    await asyncio.sleep(3)
    await Cexc.edit("**ᴜsᴇ: /clone ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ**")
    BOT_TOKEN = message.text.split(None, 1)[1]
    try:
        await Cexc.edit("**» Tʀʏ ᴛᴏ ʙᴏᴏᴛɪɴɢ ʏᴏᴜʀ ᴄʟɪᴇɴᴛ...**")                   
        Copy = PyroGram(
            ":memory:",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="Packages"),
            in_memory=True
        )
        await Copy.start()
        User = await Copy.get_me()
        await message.reply(f"**» Tʜᴀɴᴋs ғᴏʀ ᴄʟᴏɴɴɪɴɢ ʏᴏᴜʀ ᴄʟɪᴇɴᴛ ʜᴀs ʙᴇᴇɴ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴀʀᴛᴇᴅ ᴀs {User.mention} !**")
        for conodes in ALL_MODULES:
            import_module("Packages." + conodes)
    except Exception as eo:
        await message.reply("**» Eʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ᴀɢᴀɪɴ !**")
        await Soumo.send_message(Config.SUPPORT, f"**» Cʟᴏɴɴɪɴɢ ᴇʀʀᴏʀ :** `{eo}`")
"""

import asyncio
import importlib
import os
from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client as PyroGram
from pyrogram.enums import ChatType
from Linux import App as Soumo, LOGGER
import Config

@Soumo.on_message(filters.command("clone", ["$", "!", ".", "/", "?"]))
async def cloneFuncs(Soumo: Soumo, message: Message):
    if message.chat.type != ChatType.PRIVATE:
        return await message.reply("**ᴋɪɴᴅʟʏ ᴜsᴇ ɪɴ ᴘʀɪᴠᴀᴛᴇ !**")

    Cexc = await message.reply("**» Sᴛᴀʀᴛɪɴɢ ᴘʀᴏᴄᴄᴇss ᴋɪɴᴅʟʏ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...**")
    await asyncio.sleep(3)
    await Cexc.edit("**ᴜsᴇ: /clone ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ**")
    BOT_TOKEN = message.text.split(None, 1)[1]
    try:
        await Cexc.edit("**» Tʀʏ ᴛᴏ ʙᴏᴏᴛɪɴɢ ʏᴏᴜʀ ᴄʟɪᴇɴᴛ...**")

        Copy = PyroGram(
            ":memory:",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=BOT_TOKEN,
            in_memory=True
        )
        await Copy.start()
        User = await Copy.get_me()
        await message.reply(f"**» Tʜᴀɴᴋs ғᴏʀ ᴄʟᴏɴɴɪɴɢ ʏᴏᴜʀ ᴄʟɪᴇɴᴛ ʜᴀs ʙᴇᴇɴ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴀʀᴛᴇᴅ ᴀs {User.mention} !**")

        # Dynamically import modules from directory
        module_path = "Packages"
        for module_file in os.listdir(module_path):
            if module_file.endswith(".py") and not module_file.endswith("__init__.py"):
                module_name = module_file[:-3]
                module = importlib.import_module(f"{module_path}.{module_name}")
                LOGGER.info(module)

    except Exception as eo:
        await message.reply("**» Eʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ᴀɢᴀɪɴ !**")
        await Soumo.send_message(Config.SUPPORT, f"**» Cʟᴏɴɴɪɴɢ ᴇʀʀᴏʀ :** `{eo}`")
