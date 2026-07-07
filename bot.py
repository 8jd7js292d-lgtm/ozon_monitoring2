import os
import asyncio
import json

from aiogram import Bot, Dispatcher
from aiogram.types import Message


TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

FILE = "products.json"


def load_products():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_products(products):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)


@dp.message()
async def handler(message: Message):

    if not message.text:
        return

    text = message.text

    if text.startswith("/add"):

        url = text.replace("/add", "").strip()

        products = load_products()

        products.append({
            "url": url,
            "name": "Товар Ozon",
            "price": 0
        })

        save_products(products)

        await message.answer(
            "✅ Товар сохранён"
        )

    elif text == "/list":

        products = load_products()

        if not products:
            await message.answer("Список пуст")
            return

        answer = "📦 Товары:\n\n"

        for p in products:
            answer += f"{p['url']}\n\n"

        await message.answer(answer)

    else:

        await message.answer(
            "Команды:\n"
            "/add ссылка\n"
            "/list"
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())