import io
import sys
import Config
import traceback
from Linux import app
from telethon.sync import events

prexes = r"[?/.!$]"
command = r"x ?(.*)"
parsces = f"^{prexes}{command}"
app_users = Config.SUDOERS

@app.on(events.NewMessage(from_users=app_users, pattern=parsces))
async def evalFunc(event):
    if event.fwd_from:
        return
    commd = "".join(event.message.message.split(maxsplit=1)[1:])
    if not commd:
        return
    ceven = await app.send_message(event.chat.id, "<b>ʀᴜɴɴɪɴɢ...</b>", parse_mode='html')
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(commd, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation += exc
    elif stderr:
        evaluation += stderr
    elif stdout:
        evaluation += stdout
    else:
        evaluation += "sᴜᴄᴄᴇss"
    aoupu = f"<b>ᴇᴠᴀʟ ɪɴᴘᴜᴛ:</b>\n<pre>{commd}</pre>\n<b>ʀᴇsᴜʟᴛ:</b>\n<pre>{evaluation}</pre>"
    MAX_MESSAGE_SIZE_LIMIT = 69666669
    if len(aoupu) > MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(aoupu)) as ous_push:
            ous_push.name = "exec.py"
            await app.send_file(
                event.chat_id,
                ous_push,
                force_document=True,
                allow_cache=False,
                caption=f"<pre>{commd}</pre>",
                parse_mode='html'
            )
    else:
        await ceven.edit(aoupu, parse_mode='html')

async def aexec(code, smessatatus):
    message = event = smessatatus

    def p(_x):
        return print(slitu.yaml_format(_x))

    reply = await event.get_reply_message()
    user = await event.get_sender()
    chat = await event.get_chat()
    exec(
        "async def __aexec(message, reply, user, chat, app, p): "
        + "\n event = smessatatus = message"
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](message, reply, user, chat, app, p)

"""
async def aexec(code, event, app):
    msg = event
    reply = await event.get_reply_message()
    user = await event.get_sender()
    chat = await event.get_chat()
    exec(
        "async def __aexec(msg, reply, user, chat, app): "
        + "\n p = print"
        + "\n msg = event"
        + "".join(f"\n {a}" for a in code.split("\n"))
    )
    return await locals()["__aexec"](msg, reply, user, chat, app)
"""
