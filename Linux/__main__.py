import Config
import asyncio
import traceback
from telegram import Update
from Linux import Loop, pyApp, app
from importlib import import_module
from Linux.Modules import ALL_MODULES

for Modes in ALL_MODULES:
    import_module("Linux.Modules." + Modes)

def pyRun() -> None:
    print("» Pʏᴛʜᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴄʟɪᴇɴᴛ ʟᴀʏᴇʀ sᴛᴀʀᴛᴇᴅ !")
    pyApp.run_polling(
        timeout=15,
        drop_pending_updates=True,
        allowed_updates=Update.MESSAGE
    )

if __name__ == "__main__":
    try:
        app.start(bot_token=Config.BOT_TOKEN)
        secPy_Run()
    except KeyboardInterrupt:
        pass
    except Exception:
        errors = traceback.format_exc()
        print(errors)
    finally:
        try:
            if Loop.is_running():
                Loop.stop()
        finally:
            Loop.close()
