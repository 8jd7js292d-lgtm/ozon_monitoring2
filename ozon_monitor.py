import aiohttp


async def check_ozon(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            html = await response.text()

    return [
        f"Ответ Ozon получен",
        f"Размер страницы: {len(html)} символов"
    ]