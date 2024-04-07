import Config
from Mongo import *
from Linux import *
from pyrogram import *
from pyrogram.types import *
from pyrogram.enums import *

welcome_message = """
**Welcome {}**
**Prepare to embark on an extraordinary journey in the world of hunters, where the weak become strong and legends are born !**
**Get ready to delve into the depths of dungeons, face fearsome monsters, and uncover ancient mysteries that await you !**
**It's time to awaken your latent powers, hone your skills, and rise through the ranks to become the greatest hunter of them all !**
**Are you excited to start your adventure? Let your courage guide you as you step into the unknown !**
**May your determination be unyielding, your spirit unwavering, as you carve your path towards greatness in the world of hunters !**

**Let the adventure begin !**
"""
congratulations_message = """
**🎉 Congratulations on starting your adventure !**

**As a token of appreciation, here are some coins and gems to aid you on your journey :**
    **🪙 Coins :** `2500`
    **💎 Gems :** `100`
    **⚙️ Manna :** `15`
    
Use them wisely and may they help you in your quests ahead !
"""
goodbye_message = """
**Goodbye {} !**
**Should you ever decide to embark on this journey, know that the world of hunters awaits your return !
**Until we meet again, may your adventures be filled with excitement and discovery !**
"""

@App.on_message(filters.command("register"))
async def register_function(app: App, message: Message):
    user = message.from_user
    chat = message.chat
    if chat.type != ChatType.PRIVATE:
        if not await check_user(user.id):
            await message.reply("**Register Your Adventure In PM !**")
        else:
             await message.reply("**You Already Registered !**")
    else:
        if await check_user(user.id):
            await message.reply("**You Already Registered !**")                                                                                
        else:
            await message.reply_photo(
                photo="https://graph.org/file/c6759a962cfd7119199e6.jpg",
                caption=welcome_message.format(user.mention),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🚀 Embark Now", callback_data="start_adven"),
                            InlineKeyboardButton("🕒 Maybe Later", callback_data="pass_adven")
                        ]
                    ]
                )
            )

@App.on_callback_query()
async def callback_data_register(app: App, query: CallbackQuery):
    data = query.data
    if data == "satrt_adven":
        await query.message.delete()
        await add_user(query.from_user.id, user.from_user.first_name)
        await app.send_photo(
            chat_id=query.from_user.id,
            photo="https://graph.org/file/f0d03aa105aafd89a5ccc.jpg",
            caption=congratulations_message
        )
        return
    elif data == "pass_adven":
        await query.message.delete()
        await app.send_photo(
            chat_id=query.from_user.id,
            photo="https://graph.org/file/03a1495ef6bd02958b1f4.jpg",
            caption=goodbye_message
        )
        return 
