import io
import re
import os
import sys
import json
import html
import Config
import aiohttp
import asyncio
import requests
import traceback
import contextlib
import cloudscraper
from time import time
from Graph import mongo
from pyrogram import filters
from Linux import App as app
from bs4 import BeautifulSoup
from inspect import getfullargspec
from pyrogram.enums import ParseMode
from typing import Optional, Tuple, Any
from Graph.WebScrap import WebScrap, Fetch
from pyrogram.errors import MessageTooLong
from Graph.eval_Helper import format_exception, myEval
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

var = {}
teskode = {}

def readable_Time(seconds: int) -> str:
    result = ""
    (days, remainder) = divmod(seconds, 86400)
    days = int(days)
    if days != 0:
        result += f"{days}ᴅ:"
    (hours, remainder) = divmod(remainder, 3600)
    hours = int(hours)
    if hours != 0:
        result += f"{hours}ʜ:"
    (minutes, seconds) = divmod(remainder, 60)
    minutes = int(minutes)
    if minutes != 0:
        result += f"{minutes}ᴍ:"
    seconds = int(seconds)
    result += f"{seconds}s"
    return result

async def eos_Send(msg, **kwargs):
    func = msg.edit if msg.from_user.is_self else msg.reply
    spec = getfullargspec(func.__wrapped__).args
    await func(**{k: v for k, v in kwargs.items() if k in spec})

@app.on_message((filters.command("ex", Config.PREFIXS) | filters.regex(r"app.run\(\)$")) & filters.user(Config.SUDOERS))
@app.on_edited_message((filters.command("ex", Config.PREFIXS) | filters.regex(r"app.run\(\)$")) & filters.user(Config.SUDOERS))
async def exece_Terms(app:app, msg:Message) -> Optional[str]:
    if (msg.command and len(msg.command) == 1) or msg.text == "app.run()":
        return await eos_Send(msg, text="**ɴᴏ ᴇᴠᴀʟᴜᴀᴛᴇ ᴍᴇssᴀɢᴇ ғᴏᴜɴᴅ !**")
    message = await msg.reply("**ᴘʀᴏᴄᴇssɪɴɢ ᴄᴏᴅᴇ...**")
    code = msg.text.split(maxsplit=1)[1] if msg.command else msg.text.split("\napp.run()")[0]
    out_code = io.StringIO()
    out = ""
    human = readable_Time
    reply_by = msg
    if msg.reply_to_message:
        reply_by = msg.reply_to_message
    sticker = reply_by.sticker.file_id if hasattr(reply_by, 'sticker') and reply_by.sticker else None
    user = reply_by.from_user if hasattr(reply_by, 'from_user') and reply_by.from_user else reply_by
    async def _eval() -> Tuple[str, Optional[str]]:
        async def send(*args: Any, **kwargs: Any) -> Message:
            return await msg.reply(*args, **kwargs)
        # ᴘʀɪɴᴛ ᴡʀᴀᴘᴘᴇʀ ᴛᴏ ᴄᴀᴘᴛᴜʀᴇ ᴏᴜᴛᴘᴜᴛ
        # ᴡᴇ ᴅᴏɴ'ᴛ ᴏᴠᴇʀʀɪᴅᴇ sʏs.sᴛᴅᴏᴜᴛ ᴛᴏ ᴀᴠᴏɪᴅ ɪɴᴛᴇʀғᴇʀɪɴɢ ᴡɪᴛʜ ᴏᴛʜᴇʀ ᴏᴜᴛᴘᴜᴛ
        def _print(*args: Any, **kwargs: Any) -> None:
            if "file" not in kwargs:
                kwargs["file"] = out
            return print(*args, **kwargs)

        def _help(*args: Any, **kwargs: Any) -> None:
            with contextlib.redirect_stdout(out_code):
                help(*args, **kwargs)

        eval_vars = {
            "app": app,
            "humantime": human,
            "msg": msg,
            "m": msg,
            "db": mongo,
            "var": var,
            "teskode": teskode,
            "re": re,
            "os": os,
            "user": user,
            "sticker": sticker,
            "ParseMode": ParseMode,
            "sendMsg": app.send_message,
            "copyMsg": app.copy_message,
            "forwardMsg": app.forward_messages,
            "sendPhoto": app.send_photo,
            "sendVideo": app.send_video,
            "deleteMsg": app.delete_messages,
            "pinMsg": app.pin_chat_message,
            "MARKDOWN": ParseMode.MARKDOWN,
            "HTML": ParseMode.HTML,
            "IKB": InlineKeyboardButton,
            "IKM": InlineKeyboardMarkup,
            "asyncio": asyncio,
            "cloudscraper": cloudscraper,
            "json": json,
            "aiohttp": aiohttp,
            "print": _print,
            "send": send,
            "stdout": out_code,
            "traceback": traceback,
            "webscrap": WebScrap,
            "fetch": Fetch,
            "reply": msg.reply_to_message,
            "requests": requests,
            "soup": BeautifulSoup,
            "help": _help,
        }
        eval_vars.update(var)
        eval_vars.update(teskode)
        try:
            return "", await myEval(code, globals(), **eval_vars)
        except Exception as eo:
            # Fɪɴᴅ ғɪʀsᴛ ᴛʀᴀᴄᴇʙᴀᴄᴋ ғʀᴀᴍᴇ ɪɴᴠᴏʟᴠɪɴɢ ᴛʜᴇ sɴɪᴘᴘᴇᴛ
            first_snip_idx = -1
            tb = traceback.extract_tb(eo.__traceback__)
            for i, frame in enumerate(tb):
                if frame.filename == "<string>" or frame.filename.endswith("ast.py"):
                    first_snip_idx = i
                    break
            # Rᴇ-ʀᴀɪsᴇ ᴇxᴄᴇᴘᴛɪᴏɴ ɪғ ɪᴛ ᴡᴀsɴ'ᴛ ᴄᴀᴜsᴇᴅ ʙʏ ᴛʜᴇ sɴɪᴘᴘᴇᴛ
            # Rᴇᴛᴜʀɴ ғᴏʀᴍᴀᴛᴛᴇᴅ sᴛʀɪᴘᴘᴇᴅ ᴛʀᴀᴄᴇʙᴀᴄᴋ
            stripped_tb = tb[first_snip_idx:]
            formatted_tb = format_exception(eo, tb=stripped_tb)
            return "⚠️ ᴇʀʀᴏʀ ᴡʜɪʟᴇ ᴇxᴇᴄᴜᴛɪɴɢ sɴɪᴘᴘᴇᴛ\n\n", formatted_tb

    before = time()
    prefix, result = await _eval()
    after = time()
    # Aʟᴡᴀʏs ᴡʀɪᴛᴇ ʀᴇsᴜʟᴛ ɪғ ɴᴏ ᴏᴜᴛᴘᴜᴛ ʜᴀs ʙᴇᴇɴ ᴄᴏʟʟᴇᴄᴛᴇᴅ ᴛʜᴜs ғᴀʀ
    if not out_code.getvalue() or result is not None:
        print(result, file=out_code)
    el_us = after - before
    try:
        el_str = readable_Time(el_us)
    except:
        el_str = "1s"
    if not el_str or el_str is None:
        el_str = "0.1s"
    out = out_code.getvalue()
    # Sᴛʀɪᴘ ᴏɴʟʏ ONE ғɪɴᴀʟ ɴᴇᴡʟɪɴᴇ ᴛᴏ ᴄᴏᴍᴘᴇɴsᴀᴛᴇ ғᴏʀ ᴏᴜʀ ᴍᴇssᴀɢᴇ ғᴏʀᴍᴀᴛᴛɪɴɢ
    if out.endswith("\n"):
        out = out[:-1]
    try:
        success = f"{prefix}**ɪɴᴘᴜᴛ:**\n<pre>{code}</pre>\n**ᴏᴜᴛᴘᴜᴛ:**\n<pre>{out}</pre>\n**ᴇxᴇᴄᴜᴛᴇᴅ ᴛɪᴍᴇ:** {el_str}"
        await eos_Send(msg, text=success)
        await message.delete()
    except MessageTooLong:
        with io.BytesIO(str.encode(success)) as Zeep:
            Zeep.name = "LinuxTerm.txt"
            await msg.reply_document(
                document=Zeep,
                caption=f"**ᴇᴠᴀʟ:**\n<pre language='python'>{code}</pre>\n\n**ʀᴇsᴜʟᴛ:**\nᴀᴛᴛᴀᴄʜᴇᴅ ᴅᴏᴄᴜᴍᴇɴᴛ ɪɴ ғɪʟᴇ !",
                disable_notification=True,
                thumb="Graph/Templates/Pexels.jpg",
                reply_to_message_id=reply_by.id
            )
        await message.delete()
    return
    
async def aexec(code, app, msg):
    exec(
        "async def __aexec(app, msg): "
        + "\n p = print"
        + "\n replied = msg.reply_to_message"
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](app, msg)
