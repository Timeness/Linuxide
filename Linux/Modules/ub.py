import asyncio
import io
import sys
import Config
import traceback
from datetime import datetime
from pyrogram import filters, Client
from pyrogram.types import Message
from Linux.Modules.runCode import aexec

app2 = Client(
    name="pyUB2",
    api_id=29400566,
    api_hash="8fd30dc496aea7c14cf675f59b74ec6f",
    in_memory=True,
    session_string="BQHAnfYApkwzbO2p_7lfkmzMnQZO56_H3jQSSdrGeqEexnjM5NKHA67RcR_FCxFpKh3-ekqnuUQbZb5_0mY4YFyL_4nwZ6kVC0RGvpJuqE2LS42O_z4myav28IELCdXuxSdbom9-ZkqGzbh2idDD8IqgSiX6M29a9ToXSbyKPozQOTlO62d95pJ6oLOBGYQhWo1vL2x4fRP511rQu0_dxB9T2a1TUyDb8BFMUAYeY4XFbBa5vMhYypSZBNlFTCt6_35K9w7n8PkNFb7snAEafG8vnT_QVSGIEQPYkHqiSVexy4HKUYkcEmbAk5Txhf4h3L8HG4y2PsoriENBkYW5zpwyKppyDQAAAAGDvCC_AA",
    plugins=dict(root="Linux")
)

@app2.on_message(filters.command("p2", Config.PREFIXS))
@app2.on_edited_message(filters.command("p2", Config.PREFIXS))
async def runPyro_Funcs(app:app2, msg:Message) -> None:
    code = msg.text.split(None, 1)
    if len(code) == 1:
        return await msg.reply(" ᴄᴏᴅᴇ ɴᴏᴛ ғᴏᴜɴᴅ !")
    message = await msg.reply("ʀᴜɴɴɪɴɢ...")
    soac = datetime.now()
    osder = sys.stderr
    osdor = sys.stdout
    redr_opu = sys.stdout = io.StringIO()
    redr_err = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        vacue = await aexec(code[1], app, msg)
    except Exception:
        exc = traceback.format_exc()
    stdout = redr_opu.getvalue()
    stderr = redr_err.getvalue()
    sys.stdout = osdor
    sys.stderr = osder
    evason = exc or stderr or stdout or vacue or "ɴᴏ ᴏᴜᴛᴘᴜᴛ"
    eoac = datetime.now()
    runcs = (eoac - soac).microseconds / 1000
    oucode = f"📎 ᴄᴏᴅᴇ:\n{code[1]}\n📒 ᴏᴜᴛᴘᴜᴛ:\n{evason}\n✨ ᴛɪᴍᴇ ᴛᴀᴋᴇɴ: {runcs}ᴍɪʟɪsᴇᴄᴏɴᴅ"
    if len(oucode) > 69696969:
        await message.edit("⚠️ ᴏᴜᴛᴘᴜᴛ ᴛᴏᴏ ʟᴏɴɢ...")
    else:
        await message.edit(oucode)

async def soUser() -> None:
    await app2.start()

asyncio.create_task(soUser())
