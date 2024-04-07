import Config
from Mongo import *
from Linux import *
from pyrogram import *
from pyrogram.types import *
from pyrogram.enums import *

@App.on_message(filters.command("start"))
async def startFunc(app: App, update: Message):
    referred = update.text.split(None, 1)[1]
    user = update.from_user
    chat = update.chat
    if chat.type != ChatType.PRIVATE:
        if not await check_user(user.id):
            await update.reply(
                "**You Haven't /register Bot Yet Pm Me I Will Prepare You To Start Your Adventure !**",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Let's Go", url="https://telegram.me/Test_bot_of_solo_leveling_bot?start=True")]]
                )
            )
        else:
            await update.reply(
                "**You Already Started Your Adventure !**"
            )                        
    else:
        if not await check_user(user.id):
            if len(update.command) < 2:
                return await update.reply("**You haven't started bot yet so kindly /register first !**")
            try:
                ruser = await app.get_chat(referred)
                check = await user_data(ruser.id)
                await user.update_one({"user_id": ruser.id}, {"$set": {"referral": check["referral"] + 1}})
                await user.update_one({"user_id": ruser.id}, {"$set": {"coins": check["coins"] + 5000}})
                await app.send_message(ruser.id, f"✨ {user.first_name} Started Bot Via Your Referral Link After {user.first_name}'s Register You Will Get 5000 🪙 Coins As Reward !")
                await user.update_one({"user_id": ruser.id}, {"$set": {"referral_reward": check["referral_reward"] + 1}})
                await add_user(usewr.id, user.first_name)
                ucheck = await user_data(user.id)
                await user.update_one({"user_id": user.id}, {"$set": {"invited": ruser.first_name}})
                await user.update_one({"user_id": user.id}, {"$set": {"coins": ucheck["coins"] + 1500}})
                return await update.reply(f"**You are referred by {ruser.first_name} but you haven't started bot yet so kindly /register first !**")
            except Exception:
                return await update.reply("**You haven't started bot yet so kindly /register first !**")
        else:
            await update.reply(
                "**You Already Started Your Adventure !**"
            )
