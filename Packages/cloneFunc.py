import Config
import asyncio
from pyrogram import filters
from Linux import App as Soumo
from pyrogram.types import Message
from pyrogram import Client as PyroGram
from pyrogram.enums import ChatType

@Soumo.on_message(filters.command("clone", ["$", "!", ".", "/", "?"]))
async def cloneFuncs(Soumo:Soumo, message:Message):
    if message.chat.type != ChatType.PRIVATE:
        return await message.reply("**ᴋɪɴᴅʟʏ ᴜsᴇ ɪɴ ᴘʀɪᴠᴀᴛᴇ !**")
    Cexc = await message.reply("**» Sᴛᴀʀᴛɪɴɢ ᴘʀᴏᴄᴄᴇss ᴋɪɴᴅʟʏ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...**")
    await asyncio.sleep(3)
    await Cexc.edit("**ᴜsᴇ: /clone ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ**")
    BOT_TOKEN = message.text.split(None, 1)[1]
    try:
        await Texc.edit("**» Tʀʏ ᴛᴏ ʙᴏᴏᴛɪɴɢ ʏᴏᴜʀ ᴄʟɪᴇɴᴛ...**")                   
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
    except Exception as eo:
        await message.reply("**» Eʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ᴀɢᴀɪɴ !**")
        await Soumo.send_message(Config.SUPPORT, f"**» Cʟᴏɴɴɪɴɢ ᴇʀʀᴏʀ :** `{eo}`")
