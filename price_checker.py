import aiohttp
import re


async def get_price(url):

    async with aiohttp.ClientSession() as session:

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        async with session.get(
            url,
            headers=headers
        ) as response:

            text = await response.text()


    prices = re.findall(
        r'[\d\s]+₽',
        text
    )

    if prices:
        price = (
            prices[0]
            .replace(" ", "")
            .replace("₽", "")
        )

        return int(price)

    return 0