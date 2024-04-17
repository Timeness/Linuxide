import uuid
import requests
from hydrogram import *
from hydrogram.types import *
from Linux import *

shortner = {}

def shorten_v0(sur):
    api_data = "https://api-ssl.bitly.com/v4/shorten"
    access_token = "d54b6be1f251db109448bd73511e35266781b789"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "long_url": sur
    }
    response = requests.post(api_data, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["link"]
    else:
        return "ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ sʜᴏʀᴛᴇɴɪɴɢ ᴛʜᴇ ᴜʀʟ."

def shorten_v1(sur):
    api_data = "https://api.shorte.st/v1/data/url"
    data = {
        "urlToShorten": sur
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(api_data, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["shortenedUrl"]
    else:
        return "ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ sʜᴏʀᴛᴇɴɪɴɢ ᴛʜᴇ ᴜʀʟ."

def shorten_v2(sur):
    api_data = "https://v.gd/create.php"
    params = {
        "format": "simple",
        "url": sur
    }
    response = requests.get(api_data, params=params)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ sʜᴏʀᴛᴇɴɪɴɢ ᴛʜᴇ ᴜʀʟ."

def shorten_v3(sur):
    api_data = "https://u.nu/api.php?action=shorturl"
    data = {
        "url": sur
    }
    response = requests.post(api_data, data=data)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ sʜᴏʀᴛᴇɴɪɴɢ ᴛʜᴇ ᴜʀʟ."

def shorten_v4(sur):
    api_data = "https://cutt.ly/api/api.php"
    data = {
        "url": sur
    }
    response = requests.post(api_data, data=data)
    if response.status_code == 200:
        shortened_data = response.json()["url"]
        if shortened_data["status"] == 7:
            return shortened_data["shortLink"]
        else:
            return "ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ sʜᴏʀᴛᴇɴɪɴɢ ᴛʜᴇ ᴜʀʟ."
    else:
        return "ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ sʜᴏʀᴛᴇɴɪɴɢ ᴛʜᴇ ᴜʀʟ."

def shorten_v5(sur):
    api_data = "https://git.io/create"
    data = {
        "url": sur
    }
    response = requests.post(api_data, data=data)
    if response.status_code == 201:
        return response.headers["Location"]
    else:
        return "ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ sʜᴏʀᴛᴇɴɪɴɢ ᴛʜᴇ ᴜʀʟ."

def shorten_v6(sur):
    api_data = "https://snipli.com/api/v1/shorten"
    data = {
        "url": sur
    }
    response = requests.post(api_data, json=data)
    if response.status_code == 200:
        return response.json()["short"]
    else:
        return "ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ sʜᴏʀᴛᴇɴɪɴɢ ᴛʜᴇ ᴜʀʟ."

def shorten_v7(sur):
    api_data = "http://tiny.cc/ajax.php"
    params = {
        "c": "rest_api",
        "m": "shorten",
        "format": "json",
        "url": sur
    }
    response = requests.get(api_data, params=params)
    if response.status_code == 200:
        return response.json()["results"]["short_url"]
    else:
        return "ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ sʜᴏʀᴛᴇɴɪɴɢ ᴛʜᴇ ᴜʀʟ."

def shorten_v8(sur):
    api_data = "https://clck.ru/--?url="
    response = requests.get(api_data + sur)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ sʜᴏʀᴛᴇɴɪɴɢ ᴛʜᴇ ᴜʀʟ."

def shorten_v9(sur):
    api_data = "http://tinyurl.com/api-create.php?url="
    response = requests.get(api_data + sur)
    if response.status_code == 200:
        return response.text
    else:
        return "ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ sʜᴏʀᴛᴇɴɪɴɢ ᴛʜᴇ ᴜʀʟ."

def shorten_v10(sur):
    api_data = "https://is.gd/create.php"
    params = {
        "format": "json",
        "url": sur
    }
    response = requests.get(api_data, params=params)
    if response.status_code == 200:
        return response.json()["shorturl"]
    else:
        return "ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ sʜᴏʀᴛᴇɴɪɴɢ ᴛʜᴇ ᴜʀʟ."

def shorten_v11(sur):
    api_data = "https://cleanuri.com/api/v1/shorten"
    data = {
        "url": sur
    }
    response = requests.post(api_data, data=data)
    if response.status_code == 200:
        return response.json()["result_url"]
    else:
        return "ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ sʜᴏʀᴛᴇɴɪɴɢ ᴛʜᴇ ᴜʀʟ."

def shorten_v12(sur):
    api_data = "https://0x0.st/api/shorten"
    data = {
        "url": sur
    }
    response = requests.post(api_data, data=data)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ sʜᴏʀᴛᴇɴɪɴɢ ᴛʜᴇ ᴜʀʟ."


SHORTNER_PHOTO = "https://graph.org/file/ac562561b744fb415bf97.jpg"
SHORTNER_TEXT = "ᴋɪɴᴅʟʏ ᴄʜᴏᴏsᴇ ᴏɴᴇ ᴏғ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴜʀʟ sʜᴏʀᴛᴇɴɪɴɢ sᴇʀᴠɪᴄᴇ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴀɴᴅ ʏᴏᴜʀ sᴇʟᴇᴄᴛᴇᴅ sᴇʀᴠɪᴄᴇ ᴡɪʟʟ ɢᴇɴᴇʀᴀᴛᴇ ᴀ sʜᴏʀᴛᴇɴᴇᴅ ʟɪɴᴋ ғᴏʀ ʏᴏᴜ :"
SHORTNER_KEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("sʜᴏʀᴛᴇ.sᴛ", callback_data="shorte_ner"),
            InlineKeyboardButton("ᴠ.ɢᴅ", callback_data="vgd_ner")
        ],
        [
            InlineKeyboardButton("ᴜ.ɴᴜ", callback_data="unu_ner"),
            InlineKeyboardButton("ᴄᴜᴛᴛ.ʟʏ", callback_data="cutty_ner")
        ],
        [
            InlineKeyboardButton("ɢɪᴛ.ɪᴏ", callback_data="gitio_ner"),
            InlineKeyboardButton("sɴɪᴘʟɪ.ᴄᴏᴍ", callback_data="snipli_ner")
        ],
        [
            InlineKeyboardButton("ᴛɪɴʏ.ᴄᴄ", callback_data="tinycc_ner"),
            InlineKeyboardButton("ᴄʟᴄᴋ.ʀᴜ", callback_data="clckru_ner")
        ],
        [
            InlineKeyboardButton("ᴛɪɴʏᴜʀʟ.ᴄᴏᴍ", callback_data="tinyur_ner"),
            InlineKeyboardButton("ɪs.ɢᴅ", callback_data="isgd_ner")
        ],
        [
            InlineKeyboardButton("ᴄʟᴇᴀɴᴜʀɪ.ᴄᴏᴍ", callback_data="clean_ner"),
            InlineKeyboardButton("𝟶x𝟶.sᴛ", callback_data="locxst_ner")
        ]
    ]
)

@Sakura.on_message(filters.command("shortner"))
async def shorten_weburls(app: Sakura, message: Message) -> None:
    if len(message.command) == 1:
        return await message.reply("ɴᴏ ᴜʀʟ's ғᴏᴜɴᴅ ғᴏʀ sʜᴏʀᴛɴᴇʀ !")
    shorts = message.text.split(None, 1)[1]
    user_data = f"shortner_{message.from_user.id}"
    shortner[message.from_user.id] = shorts
    await message.reply_photo(
        photo=SHORTNER_PHOTO,
        caption=SHORTNER_TEXT,
        reply_markup=SHORTNER_KEYBOARD
    )

@Sakura.on_callback_query()
async def callback_query(app: Sakura, query: CallbackQuery):
    #shorts = query.message.text.split(None, 1)[1]
    user_data = shortner.get(query.from_user.id)
    if query.data == "shorte_ner":
        if user_data:
            get_shorts = shorten_v1(user_data)
            if get_shorts:
                await query.message.edit_caption(f"Sʜᴏʀᴛᴇɴᴇᴅ URL : {get_shorts}")
            else:
                await query.message.edit_caption("ғᴀɪʟᴇᴅ ᴛᴏ sʜᴏʀᴛᴇɴ ᴜʀʟ ! ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴇᴛᴇʀ.")
        else:
            await query.answer("ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ !", show_alert=True)
    elif query.data == "vgd_ner":
        if user_data:
            get_shorts = shorten_v2(user_data)
            if get_shorts:
                await query.message.edit_caption(f"Sʜᴏʀᴛᴇɴᴇᴅ URL : {get_shorts}")
            else:
                await query.message.edit_caption("ғᴀɪʟᴇᴅ ᴛᴏ sʜᴏʀᴛᴇɴ ᴜʀʟ ! ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴇᴛᴇʀ.")
        else:
            await query.answer("ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ !", show_alert=True)
    elif query.data == "unu_ner":
        if user_data:
            get_shorts = shorten_v3(user_data)
            if get_shorts:
                await query.message.edit_caption(f"Sʜᴏʀᴛᴇɴᴇᴅ URL : {get_shorts}")
            else:
                await query.message.edit_caption("ғᴀɪʟᴇᴅ ᴛᴏ sʜᴏʀᴛᴇɴ ᴜʀʟ ! ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴇᴛᴇʀ.")
        else:
            await query.answer("ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ !", show_alert=True)
    elif query.data == "cutty_ner":
        if user_data:
            get_shorts = shorten_v4(user_data)
            if get_shorts:
                await query.message.edit_caption(f"Sʜᴏʀᴛᴇɴᴇᴅ URL : {get_shorts}")
            else:
                await query.message.edit_caption("ғᴀɪʟᴇᴅ ᴛᴏ sʜᴏʀᴛᴇɴ ᴜʀʟ ! ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴇᴛᴇʀ.")
        else:
            await query.answer("ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ !", show_alert=True)
    elif query.data == "gitio_ner":
        if user_data:
            get_shorts = shorten_v5(user_data)
            if get_shorts:
                await query.message.edit_caption(f"Sʜᴏʀᴛᴇɴᴇᴅ URL : {get_shorts}")
            else:
                await query.message.edit_caption("ғᴀɪʟᴇᴅ ᴛᴏ sʜᴏʀᴛᴇɴ ᴜʀʟ ! ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴇᴛᴇʀ.")
        else:
            await query.answer("ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ !", show_alert=True)
    elif query.data == "snipli_ner":
        if user_data:
            get_shorts = shorten_v6(user_data)
            if get_shorts:
                await query.message.edit_caption(f"Sʜᴏʀᴛᴇɴᴇᴅ URL : {get_shorts}")
            else:
                await query.message.edit_caption("ғᴀɪʟᴇᴅ ᴛᴏ sʜᴏʀᴛᴇɴ ᴜʀʟ ! ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴇᴛᴇʀ.")
        else:
            await query.answer("ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ !", show_alert=True)
    elif query.data == "tinycc_ner":
        if user_data:
            get_shorts = shorten_v7(user_data)
            if get_shorts:
                await query.message.edit_caption(f"Sʜᴏʀᴛᴇɴᴇᴅ URL : {get_shorts}")
            else:
                await query.message.edit_caption("ғᴀɪʟᴇᴅ ᴛᴏ sʜᴏʀᴛᴇɴ ᴜʀʟ ! ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴇᴛᴇʀ.")
        else:
            await query.answer("ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ !", show_alert=True)
    elif query.data == "clckru_ner":
        if user_data:
            get_shorts = shorten_v8(user_data)
            if get_shorts:
                await query.message.edit_caption(f"Sʜᴏʀᴛᴇɴᴇᴅ URL : {get_shorts}")
            else:
                await query.message.edit_caption("ғᴀɪʟᴇᴅ ᴛᴏ sʜᴏʀᴛᴇɴ ᴜʀʟ ! ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴇᴛᴇʀ.")
        else:
            await query.answer("ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ !", show_alert=True)
    elif query.data == "tinyur_ner":
        if user_data:
            get_shorts = shorten_v9(user_data)
            if get_shorts:
                await query.message.edit_caption(f"Sʜᴏʀᴛᴇɴᴇᴅ URL : {get_shorts}")
            else:
                await query.message.edit_caption("ғᴀɪʟᴇᴅ ᴛᴏ sʜᴏʀᴛᴇɴ ᴜʀʟ ! ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴇᴛᴇʀ.")
        else:
            await query.answer("ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ !", show_alert=True)
    elif query.data == "isgd_ner":
        if user_data:
            get_shorts = shorten_v10(user_data)
            if get_shorts:
                await query.message.edit_caption(f"Sʜᴏʀᴛᴇɴᴇᴅ URL : {get_shorts}")
            else:
                await query.message.edit_caption("ғᴀɪʟᴇᴅ ᴛᴏ sʜᴏʀᴛᴇɴ ᴜʀʟ ! ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴇᴛᴇʀ.")
        else:
            await query.answer("ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ !", show_alert=True)
    elif query.data == "clean_ner":
        if user_data:
            get_shorts = shorten_v11(user_data)
            if get_shorts:
                await query.message.edit_caption(f"Sʜᴏʀᴛᴇɴᴇᴅ URL : {get_shorts}")
            else:
                await query.message.edit_caption("ғᴀɪʟᴇᴅ ᴛᴏ sʜᴏʀᴛᴇɴ ᴜʀʟ ! ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴇᴛᴇʀ.")
        else:
            await query.answer("ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ !", show_alert=True)
    elif query.data == "locxst_ner":
        if user_data:
            get_shorts = shorten_v12(user_data)
            if get_shorts:
                await query.message.edit_caption(f"Sʜᴏʀᴛᴇɴᴇᴅ URL : {get_shorts}")
            else:
                await query.message.edit_caption("ғᴀɪʟᴇᴅ ᴛᴏ sʜᴏʀᴛᴇɴ ᴜʀʟ ! ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴇᴛᴇʀ.")
        else:
            await query.answer("ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ !", show_alert=True)
