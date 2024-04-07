
import Config
from Mongo import *
from Linux import *
from pyrogram import *
from pyrogram.types import *
from pyrogram.enums import *

async def generate_referral(user: int):
    return f"https://telegram.me/Test_bot_of_solo_leveling_bot?start={user}"

@App.on_message(filters.command("referrals"))
async def referral_function(app: App, message: Message):
    user = message.from_user
    if message.chat.type != ChatType.PRIVATE:
        if not await check_user(user.id):
            return await message.reply(
                "**You Haven't /register Bot Yet Pm Me I Will Prepare You To Start Your Adventure !**",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Let's Go", url="https://telegram.me/Test_bot_of_solo_leveling_bot?start=True")]]
                )
            )
        else:
            await message.reply(
                "**Message Me Privately To View Your Invite Link**",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Get Link", url="https://telegram.me/Test_bot_of_solo_leveling_bot?start=referral_function")]]
                )
            )
            return
    else:
        if not await check_user(user.id):
            return await message.reply("**You haven't started bot yet so kindly /register first !**")
        else:
            check = await user_data(user.id)
            links = await generate_referral(user.id)
            await message.reply(
                (
                    "**Your Referral Link :**\n"
                    "  You Have Invited **{} Friends**\n"
                    "  Received Reward From **{} Friends**\n"
                    "**-** `{}`\n\n"
                    "**You Are Invited By :** {}"
                ).format(check["referral"], check["referral_reward"], links, check["invited"])
            )   
