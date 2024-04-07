import os
import shutil
import Config
import asyncio
from Gram import *
from pyrogram import *
from pyrogram.types import *

async def exece_command(command: str):
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return process.returncode, stdout.decode().strip(), stderr.decode().strip()

@App.on_message(filters.command("backup") & filters.user(Config.OWNER))
async def backup_mongo(app: App, message: Message):
    msg = await message.reply("**Backing up data....**")
    code, _, stderr = await execute_command(f"mongodump --uri {Config.MONGO}")
    if code != 0:
        return await msg.edit(f"**Failed to perform backup:** `{stderr}`")
        
    code, _, stderr = await execute_command("zip -r9 backup.zip dump/*")
    if code != 0:
        return await msg.edit(f"**Failed to create backup archive:** `{stderr}`")
    
    await message.reply("**Backup Success !**")
    await app.send_document(Config.SUPPORT, "backup.zip")
    
    shutil.rmtree("dump")
    os.remove("backup.zip")
    
    await msg.delete()
