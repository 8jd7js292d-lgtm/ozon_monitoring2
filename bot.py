import os
import json
import asyncio

from aiogram import Bot
from ozon_monitor import check_ozon


TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = 401758093  


async def main():
    bot = Bot(token=TOKEN)

    with open("products.json", "r", encoding="utf-8") as f:
        products = json.load(f)

    message = "🔎 Проверка Ozon\n\n"

    for product in products:
        prices = await check_ozon(product["url"])

        message += f"📦 {product['name']}\n"

        if prices:
            message += f"💰 Цены: {', '.join(prices)}\n\n"
        else:
            message += "Цены не найдены\n\n"

    await bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )

    await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())