import os
import folium
import phonenumbers
from Linux import Sakura
from Config import SUDOERS
from pyrogram import filters
from phonenumbers import carrier
from phonenumbers import geocoder
from pyrogram.types import Message
from opencage.geocoder import OpenCageGeocode

OPENCAGE_API_KEY = "c34066dc95ec40c3bf80974af13078b5"

@Sakura.on_message(filters.command("track", [".", "?", "/", "!", "$"]) & filters.command(SUDOERS))
async def track_Location(app:Sakura, message:Message) -> None:
    if len(message.command) == 1:
        return await message.reply("**ᴋɪɴᴅʟʏ ᴘʀᴏᴠɪᴅᴇ ᴍᴏʙɪʟᴇ ɴᴜᴍʙᴇʀ ᴡɪᴛʜ ᴄᴏᴜɴᴛʀʏ ᴄᴏᴅᴇ ᴛᴏ ᴛʀᴀᴄᴋ ᴅɪʀᴇᴄᴛ ʟᴏᴄᴀᴛɪᴏɴ !**")
    phone_number = str(message.command[1])
    
    parsed_number = phonenumbers.parse(phone_number)
    location = geocoder.description_for_number(parsed_number, "en")
    update = f"**Lᴏᴄᴀᴛɪᴏɴ :** {location}"
    service_provider = carrier.name_for_number(parsed_number, "en")
    update += f"**Sᴇʀᴠɪᴄᴇ Pʀᴏᴠɪᴅᴇʀ :** {service_provider}"
  
    geocoder = OpenCageGeocode(OPENCAGE_API_KEY)
    query = str(location)
    results = geocoder.geocode(query)
    if results and len(results) > 0:
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        update += f"**Lᴀᴛɪᴛᴜᴅᴇ :** {lat}"
        update += f"**Lᴏɴɢɪᴛᴜᴅᴇ :** {lng}"
        await message.reply(update)
        
        my_map = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=location).add_to(my_map)
        path_Locks = "Location.html"
        my_map.save(path_Locks)
        await message.reply_document(
            document=path_Locks,
            caption="**ʜᴇʀᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴘʜᴏɴᴇ ʟᴏᴄᴀᴛɪᴏɴs ᴍᴀᴘ ғɪʟᴇs !**"
        )
        os.remove(path_Locks)
    else:
        await message.reply("**ɢɪᴠᴇɴ ᴍᴏʙɪʟᴇ ɴᴜᴍʙᴇʀ's ᴅɪʀᴇᴄᴛ ʟᴏᴄᴀᴛɪᴏɴ ɴᴏᴛ ғᴏᴜɴᴅ !**")
