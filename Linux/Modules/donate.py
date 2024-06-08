import asyncio
from pyrogram.types import Message, PreCheckoutQuery
from pyrogram.handlers import PreCheckoutQueryHandler, MessageHandler
from pyrogram import Client, idle, filters, types
from pyrogram.enums import ChatType
from Linux import App as app

async def donateHandler(app:Client, message:Message) -> None:     
    amount = 1
    
    if len(message.command) > 1:
        try:
            amount = int(message.command[1])
            if amount <= 0:
                return await message.reply("Dᴏɴᴀᴛɪᴏɴ ᴀᴍᴏᴜɴᴛ ᴍᴜsᴛ ᴍᴇ ᴘᴏsɪᴛɪᴠᴇ !")
            if amount > 10000:
                return await message.reply("Tʜᴇ ᴍᴀxɪᴍᴜᴍ ᴅᴏɴᴀᴛɪᴏɴ ᴀᴍᴏᴜɴᴛ ɪs 10000.")
            messages = f"Cʜᴇᴇʀ ᴍᴇ ᴏɴ ᴡɪᴛʜ ᴀ ᴅᴏɴᴀᴛɪᴏɴ ᴏғ {amount} sᴛᴀʀs ! Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ʏᴏᴜʀ sᴜᴘᴘᴏʀᴛ !"    
        except ValueError:
            return await message.reply("Iɴᴠᴀʟɪᴅ ᴀᴍᴏᴜɴᴛ !")

    await app.send_invoice(
        chat_id=message.chat.id,
        title="Dᴏɴᴀᴛᴇ",
        description=messages,
        currency="XTR",
        prices=[types.LabeledPrice(label="Star", amount=amount)],
        payload="stars"
    )
    
async def preCheckout_queryHandler(_:Client, query:PreCheckoutQuery) -> None:
    await query.answer(ok=True)
    
async def successPays(app:Client, message:Message) -> None:
    await message.reply("Tʜᴀɴᴋs ғᴏʀ sᴜᴘᴘᴏʀᴛ ! Bᴜᴛ I ᴅᴏɴ'ᴛ ɴᴇᴇᴅ sᴛᴀʀs ғᴏʀ ɴᴏᴡ ! Tᴀᴋᴇ ɪᴛ ʙᴀᴄᴋ !")
    await app.refund_star_payment(message.from_user.id, message.successful_payment.telegram_payment_charge_id)
    
app.add_handler(MessageHandler(donateHandler, filters=filters.command("donate")))
app.add_handler(PreCheckoutQueryHandler(preCheckout_queryHandler))
app.add_handler(MessageHandler(successPays, filters=filters.successful_payment))
