import aiohttp
import re
import json


async def check_ozon(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            html = await response.text()

    prices = re.findall(
        r'"price"\s*:\s*"?(\\d+)',
        html
    )

    result = []

    for price in prices:
        if price not in result:
            result.append(price + " ₽")

    return result[:10]