import aiohttp
from bs4 import BeautifulSoup


async def check_ozon(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            html = await response.text()

    soup = BeautifulSoup(html, "lxml")

    prices = []

    for item in soup.find_all("span"):
        text = item.text.replace(" ", "")
        if "₽" in text:
            prices.append(text)

    return prices[:5]


async def main():
    result = await check_ozon(
        "https://www.ozon.ru/search/?text=iPhone"
    )

    print(result)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())