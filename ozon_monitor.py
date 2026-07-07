import aiohttp
import re


async def check_ozon(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
            "AppleWebKit/605.1.15 Safari/604.1"
        ),
        "Accept-Language": "ru-RU,ru;q=0.9"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            html = await response.text()

    prices = re.findall(r'\d[\d\s]{2,}\s?₽', html)

    clean = []

    for price in prices:
        price = price.replace(" ", "")
        if price not in clean:
            clean.append(price)

    return clean[:10]