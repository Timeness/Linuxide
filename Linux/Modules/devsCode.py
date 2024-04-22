import Config
from Linux import App
from pyrogram import filters
from pyrogram.types import Message

@App.on_message(filters.command("id", ["$","/",".","?","!"]) & filters.user(Config.SUDOERS))
async def userID_Funcs(app: App, message: Message):
    Chat = message.chat
    User = message.from_user
    Reply = message.reply_to_message
    
    TEXT = f"**[ᴍᴇssᴀɢᴇ ɪᴅ]({message.link}) :** `{message.id}`\n"
    TEXT += f"**[{User.mention}](tg://user?id={User.id}) :** `{User.id}`\n"
    if not message.command:
        message.command = message.text.split()
    if not message.command:
        message.command = message.text.split()
    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user = await app.get_chat(split)
            if not str(user.id).startswith("-100"):
                if not user.username:
                    TEXT += f"**[{user.first_name}](tg://user?id={user.id}) :** `{user.id}`\n"
                else:
                    TEXT += f"**[{user.first_name}](t.me/{user.username}) :** `{user.id}`\n"
            else:
                if not user.username:
                    try:
                        links = await app.export_chat_invite_link(user.id)
                        TEXT += f"**[{user.title}]({links}) :** `{user.id}`\n"
                    except Exception:
                        links = str(user.id).replace("-100", "")
                        TEXT += f"**[ᴄʜᴀᴛ ɪᴅ](t.me/c/{links}/10) :** `{user.id}`\n"
                else:
                    TEXT += f"**[{user.title}](t.me/{user.username}) :** `{user.id}`\n"
        except Exception:
            split = message.text.split(None, 1)[1].strip()
            if str(split).startswith("-100"):
                links = str(split).replace("-100", "")
                TEXT += f"**[ᴄʜᴀᴛ ɪᴅ](t.me/c/{links}/10) :** `{split}`\n"
            else:
                return await message.reply("**⚠️ ᴄᴏᴜʟᴅ ɴᴏᴛ ғɪɴᴅ ᴀ ᴜsᴇʀ ᴀʀᴇ ʏᴏᴜ sᴜʀᴇ ɪ'ᴠᴇ sᴇᴇɴ ᴛʜᴇᴍ ʙᴇғᴏʀᴇ ?**")
    if Reply and Reply.forward_from:
        TEXT += f"**[{Reply.forward_from.first_name}](telegram.me/{Reply.forward_from.username}) :** `{Reply.forward_from.id}`\n"
    if not Chat.username:
        Priver = await app.export_chat_invite_link(Chat.id)
        TEXT += f"**[{Chat.title}]({Priver}) :** `{Chat.id}`\n\n"
    else:
        TEXT += f"**[{Chat.title}](tg://user?id={Chat.id}) :** `{Chat.id}`\n\n"
    if not getattr(Reply, "empty", True) and not message.forward_from_chat and not Reply.sender_chat and not Reply.sticker and not Reply.photo:
        TEXT += f"**[ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪᴅ]({Reply.link}) :** `{Reply.id}`\n"
        TEXT += f"**[{Reply.from_user.mention}](tg://user?id={Reply.from_user.id}) :** `{Reply.from_user.id}`\n\n"
    if Reply and Reply.sticker:
        TEXT += f"**[ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪᴅ]({Reply.link}) :** `{Reply.id}`\n"
        TEXT += f"**[{Reply.from_user.mention}](tg://user?id={Reply.from_user.id}) :** `{Reply.from_user.id}`\n"
        TEXT += f"**[ʀᴇᴘʟʏ sᴛɪᴄᴋᴇʀ ɪᴅ]({Reply.link}) :** `{Reply.sticker.file_id}`\n\n"
    if Reply and Reply.photo:
        TEXT += f"**[ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪᴅ]({Reply.link}) :** `{Reply.id}`\n"
        TEXT += f"**[{Reply.from_user.mention}](tg://user?id={Reply.from_user.id}) :** `{Reply.from_user.id}`\n"
        TEXT += f"**[ᴘʜᴏᴛᴏ ғɪʟᴇ ɪᴅ]({Reply.link}) :** `{Reply.photo.file_id}`\n\n"
    if Reply and Reply.forward_from_chat:
        TEXT += f"**[ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪᴅ]({Reply.link}) :** `{Reply.id}`\n"
        TEXT += f"**[{Reply.from_user.mention}](tg://user?id={Reply.from_user.id}) :** `{Reply.from_user.id}`\n"
        TEXT += f"**ғᴏʀᴡᴀʀᴅᴇᴅ ᴄʜᴀɴɴᴇʟ ɪs [{Reply.forward_from_chat.title}](tg://user?id={Reply.forward_from_chat.id}) ʜᴀs ᴀɴ ɪᴅ :** `{Reply.forward_from_chat.id}`\n\n"        
    if Reply and Reply.sender_chat:
        TEXT += f"**[ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪᴅ]({Reply.link}) :** `{Reply.id}`\n"
        TEXT += f"**[{Reply.from_user.mention}](tg://user?id={Reply.from_user.id}) :** `{Reply.from_user.id}`\n"
        TEXT += f"**ʀᴇᴘʟɪᴇᴅ ᴄʜᴀᴛ/ᴄʜᴀɴɴᴇʟ ɪs [{Reply.sender_chat.title}](tg://user?id={Reply.sender_chat.id}) ʜᴀs ᴀɴ ɪᴅ :** `{Reply.sender_chat.id}`"
    await app.send_photo(Chat.id, photo=Config.GIST_IMAGE, caption=TEXT)
