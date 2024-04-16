from PIL import Image, ImageOps, ImageDraw, ImageChops, ImageFont
from hydrogram import filters
from Linux import Sakura
import asyncio, datetime

async def Markdown(app, Maker):
    if str(Maker).startswith("-100"):
        Chat = await app.get_chat(Maker)
        if Chat.username:
            Status = f"[{Chat.title}]({Chat.username})"
            return str(Status)
        else:
            Link = await app.export_chat_invite_link(Maker)
            Status = f"[{Chat.title}]({Link})"
            return str(Status)
    else:
        Status = (await app.get_chat(Maker)).mention
        return str(Status)

WELCOME_CAPTION = """
**ʜᴇʏ {} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ {} !**

» **ᴜsᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ :**
━━━━━━━━━━━━━━━━━━━━━
» **ɴᴀᴍᴇ :** {}
» **ᴜsᴇʀɴᴀᴍᴇ :** {}
» **ᴜsᴇʀ ɪᴅ :** `{}`
» **ᴍᴇᴍʙᴇʀs ᴄᴏᴜɴᴛ :** `{}`
» **ᴊᴏɪɴɪɴɢ ᴅᴀᴛᴇ :** `{}`
"""

def dt():
    now = datetime.datetime.now()
    dt_string = now.strftime("%d.%m.%Y %H:%M")
    dt_list = dt_string.split(" ")
    return dt_list

async def Circle(pfp, size=(215, 215)):
    pfp = pfp.resize(size, Image.Resampling.LANCZOS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.Resampling.LANCZOS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

async def userPhoto(photo, user) :
    temp = Image.open(Path)
    photo = Image.open(photo).convert("RGBA")
    photo = await Circle(photo,(535,535))
    soc = temp.copy()
    soc.paste(photo, (63, 130), photo)
    soc.save(f"./Graph/Upload{user}.png")
    return f"./Graph/Upload{user}.png"
  
Path = "./Graph/Welcome.png"

@Sakura.on_message(filters.new_chat_members, group=69)
async def _greetings(client, message):
    for user in message.new_chat_members:
        try:
            photo = await client.download_media(user.photo.big_file_id)
        except AttributeError:
            photo = None
        photo_path = await userPhoto(photo, user.id)
        chat_mention = await Markdown(client, message.chat.id)
        members_count = (await client.get_chat(message.chat.id)).members_count
        username = f"@{user.username}" if user.username else "ɴᴏɴᴇ"
        today = str(dt()[0])
        welcome_caption = WELCOME_CAPTION.format(
            user.mention, chat_mention, user.first_name, username, user.id,  members_count, today
        )
        msg = await client.send_photo(
            chat_id=message.chat.id,
            photo=photo_path,
            caption=welcome_caption
        )
        await asyncio.sleep(600)
        await msg.delete()
