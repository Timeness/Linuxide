import httpx
import aiohttp
import asyncio
from httpx import AsyncClient

async def WebScrap(Link: str, *args, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.get(Link, *args, **kwargs) as response:
            try:
                data = await response.json()
            except Exception:
                data = await response.text()
    return data

Fetch = AsyncClient(
    http2=True,
    verify=False,
    headers={
        "Accept-Language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edge/107.0.1418.42"
    },
    timeout=httpx.Timeout(20)
)
