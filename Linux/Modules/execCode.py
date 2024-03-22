import os
import sys
import Config
import traceback
from io import StringIO
from hydrogram import filters
from hydrogram.types import Message
from Linux import Sakura as app, LOGGER
  
async def aexec(code, app, msg, user): 
    exec( 
        "async def __aexec(app, msg, user): " 
        + "".join(f"\n {a}" for a in code.split("\n")) 
    ) 
    return await locals()["__aexec"](app, msg, user) 
  
@app.on_edited_message(filters.command("code", ["?", ".", "/", "!", "$"]) & filters.user(Config.SUDOERS)) 
@app.on_message(filters.command("code", ["?", ".", "/", "!", "$"]) & filters.user(Config.SUDOERS)) 
async def hydro_Execor(app: app, msg: Message):
    if len(msg.command) < 2: 
        return await msg.reply("**sʏɴᴛᴀx ᴇʀʀᴏʀ ɴᴏ ɪɴᴘᴜᴛ ғᴏᴜɴᴅ...**")
    cosc = await msg.reply("**ʀᴜɴɴɪɴɢ...**")
    try: 
        command = msg.text.split(maxsplit=1)[1]
    except IndexError as ecs: 
        LOGGER.info(f"» Eʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ : {ecs}")
    reply = msg
    if msg.reply_to_message:
        reply = msg.reply_to_message
    old_stderr = sys.stderr 
    old_stdout = sys.stdout 
    redirected_output = sys.stdout = StringIO() 
    redirected_error = sys.stderr = StringIO() 
    stdout, stderr, exc = None, None, None 
    try:
        user = reply.from_user if hasattr(reply, 'from_user') and reply.from_user else reply
        await aexec(command, app, msg, user) 
    except Exception: 
        exc = traceback.format_exc() 
    stdout = redirected_output.getvalue() 
    stderr = redirected_error.getvalue() 
    sys.stdout = old_stdout 
    sys.stderr = old_stderr 
    evaon = "" 
    if exc: 
        evaon += exc 
    elif stderr: 
        evaon += stderr 
    elif stdout: 
        evaon += stdout 
    else: 
        evaon += "Sᴜᴄᴄᴇss" 
    exec = f"<b>ɪɴᴘᴜᴛ:</b>\n{command}<b>ʀᴇsᴜʟᴛ:</b>\n<pre language='python'>{evaon}</pre>"
    if len(exec) > 9690000000069696:
        await cosc.edit("**⚠️ ᴏᴜᴛᴘᴜᴛ ᴛᴏᴏ ʟᴏɴɢ...**")
    else:
        await cosc.edit(exec)
