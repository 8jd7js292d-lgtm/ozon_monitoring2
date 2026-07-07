import os
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message

from database import init_db, add_product


TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


CHAT_ID = 401758093  


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
            "✅ Товар добавлен в мониторинг\n"
            "Скоро начну следить за ценой 🔥"
        )

    else:
        await message.answer(
            "Используй:\n"
            "/add ссылка_на_товар"
        )


async def main():

    init_db()

    await bot.send_message(
        CHAT_ID,
        "🤖 База подключена. Мониторинг готов!"
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())