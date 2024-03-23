import sys
import Config
import logging, asyncio, time
from telegram.ext import Application
from pyrogram import Client as PyGram
from hydrogram import Client as HyGram
from logging.handlers import RotatingFileHandler

GUARDS = []
for GUARD_USERS in Config.GUARDS:
    if not GUARD_USERS in GUARDS:
        GUARDS.append(GUARD_USERS)
        break
START_TIME = time.time()
__version__ = (
    {"version": 0.2},
    {"status": "on"}
)

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("logs.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ]
)
logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("hydrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

if not Config.API_ID:
    LOGGER.warning("» Wᴀʀɴɪɴɢ: ᴀᴘɪ_ɪᴅ ɴᴏᴛ ғᴏᴜɴᴅ ɪɴ ᴄᴏɴғɪɢ ғɪʟᴇs sʜᴜᴛᴅᴏᴡɴ ʙᴏᴛ !")
    sys.exit()
elif not Config.API_HASH:
    LOGGER.warning("» Wᴀʀɴɪɴɢ: ᴀᴘɪ_ʜᴀsʜ ɴᴏᴛ ғᴏᴜɴᴅ ɪɴ ᴄᴏɴғɪɢ ғɪʟᴇs sʜᴜᴛᴅᴏᴡɴ ʙᴏᴛ !")
    sys.exit()
elif not Config.BOT_TOKEN:
   LOGGER.warning("» Wᴀʀɴɪɴɢ: ʙᴏᴛ_ᴛᴏᴋᴇɴ ɴᴏᴛ ғᴏᴜɴᴅ ɪɴ ᴄᴏɴғɪɢ ғɪʟᴇs sʜᴜᴛᴅᴏᴡɴ ʙᴏᴛ !")
   sys.exit()

class Pyro():
    Soumo = PyGram(
        name="PyroSoumo",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins=dict(root="Packages"),
        in_memory=True
    )
App = Pyro.Soumo

class Hydro():
    Soumo = HyGram(
        name="HydroSoumo",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins={"root": "Packages"},
        in_memory=True
    )
Sakura = Hydro.Soumo

pyApp = Application.builder().token(Config.BOT_TOKEN).build()
Func = pyApp.add_handler
asyncio.get_event_loop().run_until_complete(
    asyncio.gather(pyApp.bot.initialize())
)
