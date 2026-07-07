import os
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message

from database import init_db, add_product, get_products, update_price
from price_checker import get_price


TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


CHAT_ID = 401758093  


@dp.message()
async def handler(message: Message):

    text = message.text


    if text.startswith("/add"):

        url = text.replace("/add", "").strip()

        add_product(
            url,
            "Товар Ozon",
            0
        )

        await message.answer(
            "✅ Добавил товар в мониторинг"
        )


    elif text == "/check":

        products = get_products()

        if not products:
            await message.answer(
                "Список товаров пуст"
            )
            return


        msg = "🔎 Проверка цен:\n\n"


        for product in products:

            new_price = await get_price(product["url"])

            old_price = product["price"]


            if old_price == 0:

                update_price(
                    product["url"],
                    new_price
                )

                msg += (
                    f"📦 {product['name']}\n"
                    f"Первая цена: {new_price} ₽\n\n"
                )


            elif new_price < old_price:

                drop = round(
                    (old_price-new_price)
                    / old_price * 100
                )

                update_price(
                    product["url"],
                    new_price
                )

                msg += (
                    "🔥 СКИДКА!\n"
                    f"📦 {product['name']}\n"
                    f"Было: {old_price} ₽\n"
                    f"Стало: {new_price} ₽\n"
                    f"Падение: -{drop}%\n\n"
                )


            else:

                msg += (
                    f"📦 {product['name']}\n"
                    f"Цена: {new_price} ₽\n\n"
                )


        await message.answer(msg)


    else:

        await message.answer(
            "Команды:\n"
            "/add ссылка\n"
            "/check"
        )


async def main():

    init_db()

    await bot.send_message(
        CHAT_ID,
        "🤖 Бот обновлён и готов"
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())