import io
import os
import Config
import textwrap
import traceback
from Linux import pyApp, Func
from contextlib import redirect_stdout
from telegram.constants import ParseMode
from telegram.ext import CommandHandler
from telegram import Chat, Message, Update, User
from telegram.ext import ContextTypes, PrefixHandler

def namespace_funcs(update, context):
    return {
        "__builtins__": globals()["__builtins__"],
        "bot": context.bot,
        "context": context,
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

async def code_input(update):
    if update.message.text and len(update.message.text.split()) > 1:
        code_parts = update.message.text.split(None, 1)
        code = code_parts[1]
        return code
    return ""

async def execute_code(update:Update, context:ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in Config.SUDOERS:
        return
    else:
        code = await code_input(update)
        result = await execute_code_in_namespace(update, context, code)
        await send_result(update, context, code, result)

def cleanup_code(code):
    if code.startswith("```") and code.endswith("```"):
        return "\n".join(code.split("\n")[1:-1])
    return code.strip("` \n")

async def execute_code_in_namespace(update, context, code):
    env = namespace_funcs(update, context)
    code = cleanup_code(code)
    stdout = io.StringIO()
    to_compile = f'async def func():\n{textwrap.indent(code, "  ")}'
    try:
        exec(to_compile, env)
    except Exception as e:
        return f"{e.__class__.__name__}: {e}"

    func = env["func"]
    try:
        with redirect_stdout(stdout):
            func_return = await func()
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
                    result = f"{repr(eval(code, env))}"
                except:
                    pass
        else:
            result = f"{value}{func_return}"
        if result:
            return result

async def send_result(update, context, code, result):
    if len(str(result)) > 696969:
        with io.BytesIO(result.encode()) as output:
            output.name = "TeleTerm.txt"
            await context.bot.send_document(chat_id=update.effective_chat.id, document=output)
    else:
        await update.effective_message.reply_text(
            text=f"<b>ɪɴ:</b>\n<pre>{code}</pre>\n<b>ᴏᴜᴛ:</b>\n<pre>{result}</pre>",
            parse_mode=ParseMode.HTML
        )

Func(PrefixHandler(Config.PREFIXS, "rs", execute_code))
