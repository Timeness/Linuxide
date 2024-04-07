from Linux import *
from Mongo import *
from pyrogram import *
from pyrogram.types import *
from pyrogram.enums import *

BALANCE = """
**🫧 User Balance :**

**🔱 ID :** `{}`
**🪬 User :** `{}`
**🪙 Coins :** `{}`
**💎 Gems :** `{}`
**⚙️ Manna :** `{}`
"""

@App.on_message(filters.command("balance"))
async def bala(app: App, message: Message):
    user = message.from_user
    if message.chat.type != ChatType.PRIVATE:
        if not await check_user(user):
            await message.reply(
                "**You Haven't /register Bot Yet Pm Me I Will Prepare You To Start Your Adventure !**",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Let's Go", url="https://telegram.me/Test_bot_of_solo_leveling_bot?start=True")]]
                )
            )
        else:
            check = await user_data(user.id)
            await message.reply_photo(
                photo="https://graph.org/file/f0d03aa105aafd89a5ccc.jpg",
                caption=BALANCE.format(check["user_id"], check["user_name"], check["coins"], check["gems"], check["manna"])
            )
    else:
        if not await check_user(user):
            return await update.reply("**You haven't started bot yet so kindly /register first !**")
        else:
            check = await user_data(user.id)
            await message.reply_photo(
                photo="https://graph.org/file/f0d03aa105aafd89a5ccc.jpg",
                caption=BALANCE.format(check["user_id"], check["user_name"], check["coins"], check["gems"], check["manna"])
            )
