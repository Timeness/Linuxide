import io
import os
import Config
import textwrap
import traceback
from typing import cast
from Linux import pyApp, Func
from contextlib import redirect_stdout
from telegram.constants import ParseMode
from telegram import Chat, Message, Update, User
from telegram.ext import ContextTypes, PrefixHandler

namespaces = {}

def namespace_Funcs(Chat, update, context):
    if Chat not in namespaces:
        namespaces[Chat] = {
            "__builtins__": globals()["__builtins__"],
            "bot": context.bot,
            "context": context,
            "MARKDOWN": ParseMode.MARKDOWN,
            "HTML": ParseMode.HTML,
            "ParseMode": ParseMode,
            "msg": update.effective_message,
            "user": update.effective_user,
            "chat": update.effective_chat,
            "reply": update.effective_message.reply_to_message,
            "effective_message": update.effective_message,
            "effective_user": update.effective_user,
            "effective_chat": update.effective_chat,
            "update": update,
        }
    return namespaces[Chat]

async def code_Input(update):
    xode = update.message.text.split(None, 1)
    code = xode[1]
    return code
    
async def execues_Funcs(update:Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_message.from_user.id not in Config.SUDOERS:
        return
    else:
        codes = await code_Input(update)
        await send(await do_Execs(exec, context, update), context, update, codes)
        if os.path.isfile("Graph/Hydro.txt"):
            os.remove("Graph/Hydro.txt")

def cleanup_Code(code):
    if code.startswith("```") and code.endswith("```"):
        return "\n".join(code.split("\n")[1:-1])
    return code.strip("` \n")

async def do_Execs(func, context, update):
    if not len(update.message.text.split(None, 1)) > 1:
        await update.message.reply_text("<b>ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ sᴏᴍᴇ ᴄᴏᴅᴇ !</b>", parse_mode=ParseMode.HTML)
        return
    await code_Input(update)
    content = update.message.text.split(None, 1)[1]
    body = cleanup_Code(content)
    env = namespace_Funcs(update.effective_chat.id, update, context)

    os.chdir(os.getcwd())
    with open(
        os.path.join(os.getcwd(), "Graph/Hydro.txt"), "w"
    ) as temp:
        temp.write(body)

    stdout = io.StringIO()
    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'
    try:
        exec(to_compile, env)
    except Exception as e:
        return f"{e.__class__.__name__}: {e}"

    func = env["func"]
    try:
        with redirect_stdout(stdout):
            func_return = func()
    except Exception:
        value = stdout.getvalue()
        return f"{value}{traceback.format_exc()}"
    else:
        value = stdout.getvalue()
        result = None
        if func_return is None:
            if value:
                result = f"{value}"
            else:
                try:
                    result = f"{repr(eval(body, env))}"
                except:
                    pass
        else:
            result = f"{value}{func_return}"
        if result:
            return result

async def send(message, context, update, codes):
    if len(str(message)) > 696969:
        with io.BytesIO(str.encode(message)) as ousce:
            ousce.name = "TeleTerm.txt"
            await context.bot.send_document(chat_id=update.effective_chat.id, document=ousce)
    else:
        await update.effective_message.reply_text(
            text=f"<b>ɪɴ:</b>\n<pre>{codes}</pre>\n<b>ᴏᴜᴛ:</b>\n<pre>{message}</pre>",
            parse_mode=ParseMode.HTML
        )

Func(PrefixHandler(Config.PREFIXS, "e", execues_Funcs))
