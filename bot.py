import os
import asyncio
from aiogram import Bot

TOKEN = os.getenv("BOT_TOKEN")

async def main():
    bot = Bot(token=TOKEN)
    await bot.send_message(
        chat_id=401758093,
        text="🤖 Бот запущен через GitHub Actions!"
    )
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())