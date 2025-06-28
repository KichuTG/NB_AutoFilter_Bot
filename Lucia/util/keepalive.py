import asyncio
import logging
import aiohttp
import traceback
from info import *
from info import URL

async def keep_alive():
    """Send a request every 60 seconds to keep the bot alive (if required)."""
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                await session.get(KEEP_ALIVE_URL)
                logging.info("Sent keep-alive request.")
            except Exception as e:
                logging.error(f"Keep-alive request failed: {e}")
            await asyncio.sleep(60)
