import aiohttp
import re
import html


async def check_ozon(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            page = await response.text()

    page = html.unescape(page)

    # ищем цены в скрытых данных
    prices = re.findall(r'\d{3,6}\s?₽', page)

    result = []

    for price in prices:
        price = price.replace(" ", "")
        if price not in result:
            result.append(price)

    if result:
        return result[:10]

    return ["Цены пока не найдены"]