from PIL import Image, ImageOps, ImageDraw, ImageChops, ImageFont
from hydrogram import filters
from Linux import Sakura

WELCOME_CAPTION = """
**ʜᴇʏ {} [{}] ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ {} !**

» **ᴜsᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ :**
━━━━━━━━━━━━━━━━━━━━━
» **ɴᴀᴍᴇ :** {}
» **ᴜsᴇʀɴᴀᴍᴇ :** {}
» **ᴜsᴇʀ ɪᴅ :** `{}`
» **ᴊᴏɪɴɪɴɢ ᴅᴀᴛᴇ :** `{}`
"""

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
        welcome_caption = WELCOME_CAPTION.format(
            user.mention, user.id, message.chat.title
        )
