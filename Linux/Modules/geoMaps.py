import Config
from Linux import Sakura
from pyrogram import filters
from pyrogram.types import Message
from geopy.geocoders import Nominatim
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Sakura.on_message(filters.command("geomap", [".", "?", "/", "!", "$"]) & filters.user(Config.SUDOERS))
async def geomapFuncs(app:Sakura, message:Message) -> None:
    geolocator = Nominatim(user_agent="NeoXGraph")
    if len(message.command) == 1:
        return await message.reply("**ᴘʟᴇᴀsᴇ sᴘᴇᴄɪғʏ ᴀ ɢᴇᴏᴍᴀᴘ ʟᴏᴄᴀᴛɪᴏɴ ɴᴀᴍᴇ !**")
    pushLock = message.text.split(None, 1)[1]
    try:
        geoloc = geolocator.geocode(pushLock)
        goodLock = f"https://www.google.com/maps/search/{geoloc.latitude},{geoloc.longitude}"
        markup = InlineKeyboardMarkup([[InlineKeyboardButton("Oᴘᴇɴ Iɴ 🌏 Gᴏᴏɢʟᴇ Mᴀᴘs", url=goodLock)]])
        await app.send_location(
            chat_id=message.chat.id,
            latitude=float(geoloc.latitude),
            longitude=float(geoloc.longitude),
            reply_markup=markup
        )
    except Exception:
        await message.reply("**⚠️ Gɪᴠᴇɴ ʟᴏᴄᴀᴛɪᴏɴ ɴᴏᴛ ғᴏᴜɴᴅ !**")
