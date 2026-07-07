import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message()
async def start(message: Message):
    await message.answer(
        "🤖 Бот запущен!\n"
        "Охота за скидками Ozon начинается 🔥"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())