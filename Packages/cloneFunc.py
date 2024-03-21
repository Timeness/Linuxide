from pyrogram import filters
from App import app as Soumo
from pyrogram.types import Message
from pyrogram import Client as PyroGram
from asyncio.exceptions import TimeoutError
SUPPORT = "-1001535967539"

async def CancFunc(message):
    if "/rem_clone" in message.text:
        await message.reply_text(
            "**» Cᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴩʀᴏᴄᴇss.**"
        )
        return True
    else:
        return False

@Soumo.on_message(filters.command("clone", ["C", "$", "!", ".", "/", "?"]))
async def cloneFuncs(Soumo:Soumo, message:Message):
    if message.chat.type != ChatType.PRIVATE:
        return await message.reply("**ᴋɪɴᴅʟʏ ᴜsᴇ ɪɴ ᴘʀɪᴠᴀᴛᴇ !**")
    Texc = await message.reply("**» Sᴛᴀʀᴛɪɴɢ ᴘʀᴏᴄᴄᴇss ᴋɪɴᴅʟʏ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...**")
    await asyncio.sleep(3)
    try:
        API_ID = await Soumo.ask(
            identifier=(message.chat.id, message.from_user.id, None),
            text="**» Kɪɴᴅʟʏ ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴀᴘɪ ɪᴅ ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ :**",
            filters=filters.text,
            timeout=60,
        )
    except TimeoutError:
        return await Soumo.send_message(
            message.from_user.id,
            "**» Sᴏʀʀʏ ᴛɪᴍᴇᴅ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 60 sᴇᴄᴏɴᴅs.**"
        )

    if await CancFunc(API_ID):
        return
      
    try:
        API_ID = int(API_ID.text)
    except ValueError:
        return await Soumo.send_message(
            message.from_user.id,
            "**» Sᴏʀʀʏ ᴛʜᴇ ᴀᴘɪ ɪᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ɪɴᴠᴀʟɪᴅ.**"
        )
      
    try:
        API_HASH = await Soumo.ask(
            identifier=(message.chat.id, message.from_user.id, None),
            text="» Kɪɴᴅʟʏ ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴀᴘɪ ʜᴀsʜ ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ :",
            filters=filters.text,
            timeout=60,
        )
    except TimeoutError:
        return await Soumo.send_message(
            message.from_user.id,
            "**» Sᴏʀʀʏ ᴛɪᴍᴇᴅ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 60 sᴇᴄᴏɴᴅs.**"
        )

    if await CancFunc(API_HASH):
        return

    API_HASH = API_HASH.text
    if len(API_HASH) < 30:
        return await Soumo.send_message(
            message.from_user.id,
            "**» Sᴏʀʀʏ ᴛʜᴇ ᴀᴘɪ ʜᴀsʜ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ɪɴᴠᴀʟɪᴅ.**"
        )

    try:
        BOT_TOKEN = await Soumo.ask(
            identifier=(message.chat.id, message.from_user.id, None),
            text="» Kɪɴᴅʟʏ ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ :",
            filters=filters.text,
            timeout=60,
        )
    except TimeoutError:
        return await Soumo.send_message(
            message.from_user.id,
            "**» Sᴏʀʀʏ ᴛɪᴍᴇᴅ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 60 sᴇᴄᴏɴᴅs.**"
        )

    BOT_TOKEN = BOT_TOKEN.text
    try:
        await Texc.edit("**» Tʀʏ ᴛᴏ ʙᴏᴏᴛɪɴɢ ʏᴏᴜʀ ᴄʟɪᴇɴᴛ...**")                   
        Copy = PyroGram(
            ":memory:",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="Packages"),
            in_memory=True
        )
        await Copy.start()
        User = await Copy.get_me()
        await message.reply(f"**» Tʜᴀɴᴋs ғᴏʀ ᴄʟᴏɴɴɪɴɢ ʏᴏᴜʀ ᴄʟɪᴇɴᴛ ʜᴀs ʙᴇᴇɴ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴀʀᴛᴇᴅ ᴀs {User.mention} !**")
    except Exception as eo:
        await message.reply("**» Eʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ᴀɢᴀɪɴ !**")
        await Soumo.send_message(SUPPORT, f"**» Cʟᴏɴɴɪɴɢ ᴇʀʀᴏʀ :** `{eo}`")
