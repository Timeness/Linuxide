import sys
import Config
import asyncio
from telegram import Update
from Graph import Clean_Stage
from importlib import import_module
from pyrogram import idle as PyGram
from hydrogram import idle as HyGram
from Linux.Modules import ALL_MODULES
from telegram.ext import ContextTypes
from Linux import App, Sakura, LOGGER, pyApp
from telegram.error import (
    BadRequest, ChatMigrated, Forbidden, NetworkError, TelegramError, TimedOut
)

async def addPackages():
    await App.start()
    await Sakura.start()
    for nodes in ALL_MODULES:
        import_module("Linux.Modules." + nodes)
    LOGGER.info("» Sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ ᴀʟʟ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴅᴇᴘʟᴏʏᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ !")
    try:
        Resocs = await Clean_Stage()
        if Resocs:
            await App.edit_message_text(
                Resocs["chat_id"],
                Resocs["message_id"],
                "**🔮 Lɪɴᴜxɪᴅᴇ Rᴇsᴛᴀʀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ !**"
            )
        else:
            await App.send_message(Config.SUPPORT, "**🔮 Lɪɴᴜxɪᴅᴇ Cʟᴏᴜᴅ Sᴇʀᴠᴇʀ Sᴛᴀʀᴛᴇᴅ !**")
    except Exception:
        LOGGER.info("» Bᴏᴛ ʜᴀs ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴀᴅᴅᴇᴅ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ.")
      
    await PyGram()
    await HyGram()
    await App.send_message(SUPPORT, "**🚧 Mᴀɪɴᴛᴇɴᴀɴᴄᴇ Mᴏᴅᴇ Oɴ ! Lɪɴᴜxɪᴅᴇ Is Nᴏᴡ Dᴇᴀᴅ.**")
    LOGGER.info("» Gᴏᴏᴅ Bʏᴇ Sᴛᴏᴘᴘɪɴɢ Lɪɴᴜxɪᴅᴇ !")

async def error_SysFunc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    error = context.error
    try:
        raise error
    except Forbidden:
        LOGGER.info("» Nᴏɴᴇ ! Cᴜʀʀᴇɴᴛ Tᴇsᴛ Oɴɢᴏɪɴɢ ᴠ1.")
        LOGGER.info(error)
        # ʀᴇᴍᴏᴠᴇ ᴜᴘᴅᴀᴛᴇ.ᴄʜᴀᴛ_ɪᴅ ғʀᴏᴍ ᴄᴏɴᴠᴇʀsᴀᴛɪᴏɴ ʟɪsᴛ
    except BadRequest:
        LOGGER.info("» Nᴏɴᴇ ! Cᴜʀʀᴇɴᴛ Tᴇsᴛ Oɴɢᴏɪɴɢ ᴠ2.")
        LOGGER.info("» Bᴀᴅʀᴇǫᴜᴇsᴛ Cᴀᴜɢʜᴛ !")
        LOGGER.info(error)
        # ʜᴀɴᴅʟᴇ ᴍᴀʟғᴏʀᴍᴇᴅ ʀᴇǫᴜᴇsᴛs - ʀᴇᴀᴅ ᴍᴏʀᴇ ʙᴇʟᴏᴡ !
    except TimedOut:
        LOGGER.info("» Nᴏɴᴇ ! Cᴜʀʀᴇɴᴛ Tᴇsᴛ Oɴɢᴏɪɴɢ ᴠ3.")
        # ʜᴀɴᴅʟᴇ sʟᴏᴡ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ᴘʀᴏʙʟᴇᴍs
    except NetworkError:
        LOGGER.info("» Nᴏɴᴇ ! Cᴜʀʀᴇɴᴛ Tᴇsᴛ Oɴɢᴏɪɴɢ ᴠ4.")
        # ʜᴀɴᴅʟᴇ ᴏᴛʜᴇʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ᴘʀᴏʙʟᴇᴍs
    except ChatMigrated as eorr:
        LOGGER.info("» Nᴏɴᴇ ! Cᴜʀʀᴇɴᴛ Tᴇsᴛ Oɴɢᴏɪɴɢ ᴠ5.")
        LOGGER.info(eorr)
        # ᴛʜᴇ ᴄʜᴀᴛ_ɪᴅ ᴏғ ᴀ ɢʀᴏᴜᴘ ʜᴀs ᴄʜᴀɴɢᴇᴅ ᴜsᴇ ᴇ.ɴᴇᴡ_ᴄʜᴀᴛ_ɪᴅ ɪɴsᴛᴇᴀᴅ
    except TelegramError:
        LOGGER.info(error)
        # ʜᴀɴᴅʟᴇ ᴀʟʟ ᴏᴛʜᴇʀ ᴛᴇʟᴇɢʀᴀᴍ ʀᴇʟᴀᴛᴇᴅ ᴇʀʀᴏʀs

def superPy_Run() -> None:
    LOGGER.info("» Pʏᴛʜᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴄʟɪᴇɴᴛ ʟᴀʏᴇʀ sᴛᴀʀᴛᴇᴅ !")
    pyApp.add_error_handler(error_SysFunc)
    pyApp.run_polling(timeout=15, drop_pending_updates=True, allowed_updates=Update.MESSAGE)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(addPackages())
    superPy_Run()
    LOGGER.info("» Lɪɴᴜxɪᴅᴇ sᴜᴄᴄᴇssғᴜʟʟʏ ᴀᴄᴛɪᴠᴀᴛᴇᴅ !")
