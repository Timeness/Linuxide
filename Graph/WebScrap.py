import aiohttp
import asyncio
session = aiohttp.ClientSession()

async def WebScrap(Link:str, *args, **kwargs):
    async with session.get(Link, *args, **kwargs) as response:
        try:
            data = await responce.json()
        except Exception:
            data = await responce.text()
    return data
