import os
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message

from database import (
    init_db,
    add_product,
    get_products,
    update_price
)

from price_checker import get_price


TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


CHAT_ID = 123456789  # замени на свой Telegram ID


@dp.message()
async def messages(message: Message):

    text = message.text


    if text.startswith("/add"):

        url = text.replace("/add", "").strip()

        add_product(
            url,
            "Товар Ozon",
            0
        )

        await message.answer(
            "✅ Добавил товар в мониторинг 🔥"
        )


    elif text == "/check":

        products = get_products()

        if not products:
            await message.answer(
                "Список товаров пуст"
            )
            return


        result = "🔎 Проверка цен:\n\n"


        for url, name, old_price in products:

            new_price = await get_price(url)


            if old_price == 0:

                update_price(
                    url,
                    new_price
                )

                result += (
                    f"📦 {name}\n"
                    f"Первая цена: {new_price} ₽\n\n"
                )


            elif new_price < old_price:

                drop = round(
                    (old_price - new_price)
                    / old_price * 100
                )


                update_price(
                    url,
                    new_price
                )


                result += (
                    f"🔥 СКИДКА!\n\n"
                    f"📦 {name}\n"
                    f"Было: {old_price} ₽\n"
                    f"Стало: {new_price} ₽\n"
                    f"Падение: -{drop}%\n\n"
                )


            else:

                result += (
                    f"📦 {name}\n"
                    f"Цена: {new_price} ₽\n\n"
                )


        await message.answer(result)


    else:

        await message.answer(
            "Команды:\n"
            "/add ссылка\n"
            "/check проверка"
        )



async def main():

    init_db()

    await bot.send_message(
        CHAT_ID,
        "🤖 Мониторинг обновлён!"
    )

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())