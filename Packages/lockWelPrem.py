import datetime
from Graph import db
from pyrogram import filters
from Linux import App as client
from pyrogram.types import Message


@client.on_message(filters.new_chat_members)
async def member_premium(client: client, message: Message) -> None:
    check = message.new_chat_members[0]
    user = await client.get_user(check.id)
    if await wepre.find_one({"chat_id": message.chat.id}):
        if user.is_premium:
            await client.ban_chat_member(message.chat.id, user.id)
            try:
                await message.reply(f"ᴅᴜᴇ ᴛᴏ ʟᴏᴄᴋ ᴘʀᴇᴍɪᴜᴍ ᴍᴏᴅᴇ ᴇɴᴀʙʟᴇᴅ ɪ ʙᴀɴɴᴇᴅ {user.mention} ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀ ᴛᴏ ᴊᴏɪɴ ᴛʜɪs ᴄʜᴀᴛ.")
            except Exception:
                await client.send_message(message.chat.id, f"ᴅᴜᴇ ᴛᴏ ʟᴏᴄᴋ ᴘʀᴇᴍɪᴜᴍ ᴍᴏᴅᴇ ᴇɴᴀʙʟᴇᴅ ɪ ʙᴀɴɴᴇᴅ {user.mention} ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀ ᴛᴏ ᴊᴏɪɴ ᴛʜɪs ᴄʜᴀᴛ.")
          
wepre = db["Soumo"]["PremWe"]

@client.on_message(filters.command("welcomelock"))
async def welcomeLock(client: client, message: Message) -> None:
    if len(message.command) == 1:
        return await message.reply("**• Usᴀɢᴇ sʏɴᴛᴀx: /welcomelock [ᴍᴏᴅᴇs]**")
    modes = message.text.split(None, 1)[1]
    if modes == "premium":
        if await wepre.find_one({"chat_id": message.chat.id}):
            await message.reply("**ᴡᴇʟᴄᴏᴍᴇ ʟᴏᴄᴋ ᴘʀᴇᴍɪᴜᴍ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ ʜᴇʀᴇ.**")
        else:
            await wepre.insert_one({"chat_id": message.chat.id})
            await message.reply("**ʟᴏᴄᴋᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ.**")
    else:
        await message.reply("**ᴄʜᴇᴄᴋ ᴡᴇʟᴄᴏᴍᴇ ʟᴏᴄᴋ ᴍᴏᴅᴇs.**")
  
