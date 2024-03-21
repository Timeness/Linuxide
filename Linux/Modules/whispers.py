import shortuuid
from Linux import Func
from Graph import mongo
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Update
)
from telegram.ext import CallbackQueryHandler, ContextTypes, InlineQueryHandler
wper = mongo["SoumoDB"]["whisper"]

class Whispers:
    @staticmethod
    def add_whisper(WhisperId, WhisperData):
        whisper = {"WhisperId": WhisperId, "whisperData": WhisperData}
        wper.insert_one(whisper)

    @staticmethod
    def del_whisper(WhisperId):
        wper.delete_one({"WhisperId": WhisperId})

    @staticmethod
    def get_whisper(WhisperId):
        whisper = wper.find_one({"WhisperId": WhisperId})
        return whisper["whisperData"] if whisper else None

async def main_Whisper(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query
    if not query.query:
        return await query.answer(
            [],
            switch_pm_text="ɢɪᴠᴇ ᴍᴇ ᴀ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ᴜsᴇʀɪᴅ !",
            switch_pm_parameter="ghelp_whisper",
        )
    user, message = parse_user_message(query.query)
    if len(message) > 200:
        return
    usertype = "username" if user.startswith("@") else "id"
    if user.isdigit():
        try:
            chat = await context.bot.get_chat(int(user))
            user = f"@{chat.username}" if chat.username else chat.first_name
        except Exception:
            pass

    whisperData = {
        "user": query.from_user.id,
        "withuser": user,
        "usertype": usertype,
        "type": "inline",
        "message": message,
    }
    whisperId = shortuuid.uuid()

    Whispers.add_whisper(whisperId, whisperData)
    answers = [
        InlineQueryResultArticle(
            id=whisperId,
            title=f"👤 sᴇɴᴅ ᴀ ᴡʜɪsᴘᴇʀ ᴍᴇssᴀɢᴇ ᴛᴏ {user} !",
            description="ᴏɴʟʏ ᴛʜᴇʏ ᴄᴀɴ sᴇᴇ ɪᴛ !",
            input_message_content=InputTextMessageContent(
                f"🔐 ᴀ ᴡʜɪsᴘᴇʀ ᴍᴇssᴀɢᴇ ғᴏʀ {user}\nᴏɴʟʏ ᴛʜᴇʏ ᴄᴀɴ sᴇᴇ ɪᴛ !"
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "📩 sʜᴏᴡ ᴡʜɪsᴘᴇʀ 📩",
                            callback_data=f"whisper_{whisperId}",
                        )
                    ]
                ]
            )
        )
    ]
    await context.bot.answer_inline_query(query.id, answers)

async def show_Whisper(update: Update, context: ContextTypes.DEFAULT_TYPE):
    callback_query = update.callback_query
    whisperId = callback_query.data.split("_")[-1]
    whisper = Whispers.get_whisper(whisperId)

    if not whisper:
        await context.bot.answer_callback_query(
            callback_query.id, "ᴛʜɪs ᴡʜɪsᴘᴇʀ ɪs ɴᴏᴛ ᴠᴀʟɪᴅ ᴀɴʏᴍᴏʀᴇ !"
        )
        return
    userType = whisper["usertype"]
    from_user_id = callback_query.from_user.id
    if from_user_id == whisper["user"]:
        await context.bot.answer_callback_query(
            callback_query.id, whisper["message"], show_alert=True
        )
    elif (
        userType == "username"
        and callback_query.from_user.username
        and callback_query.from_user.username.lower()
        == whisper["withuser"].replace("@", "").lower()
    ):
        await context.bot.answer_callback_query(
            callback_query.id, whisper["message"], show_alert=True
        )
    elif userType == "id" and from_user_id == int(whisper["withuser"]):
        await context.bot.answer_callback_query(
            callback_query.id, whisper["message"], show_alert=True
        )
    else:
        await context.bot.answer_callback_query(
            callback_query.id, "ɴᴏᴛ ʏᴏᴜʀ ᴡʜɪsᴘᴇʀ !", show_alert=True
        )

def parse_user_message(query_text):
    text = query_text.split(" ")
    user = text[0]
    first = True
    message = ""
    if not user.startswith("@") and not user.isdigit():
        user = text[-1]
        first = False
    if first:
        message = " ".join(text[1:])
    else:
        text.pop()
        message = " ".join(text)
    return user, message

Func(InlineQueryHandler(main_Whisper))
Func(CallbackQueryHandler(show_Whisper, pattern="^whisper_"))
