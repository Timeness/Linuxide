import asyncio
import aiohttp
from Linux import LOGGER
from Linux import App as app
from pyrogram import filters
from pyrogram.types import Message
SESSION_HEADERS = {"Host": "lexica.qewertyy.me"}

class AsyncClient:
    def __init__(self):
        self.url = "https://lexica.qewertyy.me"
        self.session = aiohttp.ClientSession()

    async def generate(self, model_id, prompt, negative_prompt):
        data = {
            "model_id": model_id,
            "prompt": prompt,
            "negative_prompt": negative_prompt if negative_prompt else "",
            "num_images": 1,
        }
        try:
            async with self.session.post(
                f"{self.url}/models/inference", data=data, headers=SESSION_HEADERS
            ) as resp:
                return await resp.json()
        except Exception as esc:
            LOGGER.info(f"» Rᴇǫᴜᴇsᴛ ғᴀɪʟᴇᴅ : {str(esc)}")

    async def get_images(self, task_id, request_id):
        data = {"task_id": task_id, "request_id": request_id}
        try:
            async with self.session.post(
                f"{self.url}/models/inference/task", data=data, headers=SESSION_HEADERS
            ) as resp:
                return await resp.json()
        except Exception as esc:
            LOGGER.info(f"» Rᴇǫᴜᴇsᴛ ғᴀɪʟᴇᴅ : {str(esc)}")


async def generate_Image_Handler(msg, model):
    command = msg.text.split(None, 1)
    if len(command) < 2:
        await msg.reply("**ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴘʀᴏᴍᴘᴛ...**")
        return
    prompt = command[1]
    negative = ""
    reply_message = await msg.reply("**ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ ɪᴍᴀɢᴇ ᴋɪɴᴅʟʏ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...**")

    client = AsyncClient()
    response = await client.generate(model, prompt, negative)
    task = response["task_id"]
    request = response["request_id"]
    while True:
        generated = await client.get_images(task, request)
        if "img_urls" in generated:
            for img_url in generated["img_urls"]:
                await reply_message.delete()
                await msg.reply_photo(img_url)
            break
        else:
            await asyncio.sleep(5)

        timeout = 600
        if timeout <= 0:
            await reply_message.edit("**ɪᴍᴀɢᴇ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴛɪᴍᴇᴅ ᴏᴜᴛ.**")
            break
        timeout -= 5

@app.on_message(filters.command("meinamix", ["?", "/", "!", ".", "$"]))
async def genera_Funcs(app, msg):
    await generate_Image_Handler(msg, model_id=2)

@app.on_message(filters.command("sushi", ["?", "/", "!", ".", "$"]))
async def genera_Funcs(app, msg):
    await generate_Image_Handler(msg, model_id=7)

@app.on_message(filters.command("meinahentai", ["?", "/", "!", ".", "$"]))
async def genera_Funcs(app, msg):
    await generate_Image_Handler(msg, model_id=8)
  
@app.on_message(filters.command("darksushimix", ["?", "/", "!", ".", "$"]))
async def genera_Funcs(app, msg):
    await generate_Image_Handler(msg, model_id=9)

@app.on_message(filters.command("anylora", ["?", "/", "!", ".", "$"]))
async def genera_Funcs(app, msg):
    await generate_Image_Handler(msg, model_id=3)

@app.on_message(filters.command("cetusmix", ["?", "/", "!", ".", "$"]))
async def genera_Funcs(app, msg):
    await generate_Image_Handler(msg, model_id=10)

@app.on_message(filters.command("darkv2", ["?", "/", "!", ".", "$"]))
async def genera_Funcs(app, msg):
    await generate_Image_Handler(msg, model_id=14)

@app.on_message(filters.command("creative", ["?", "/", "!", ".", "$"]))
async def genera_Funcs(app, msg):
    await generate_Image_Handler(msg, model_id=12)
