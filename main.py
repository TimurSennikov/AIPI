import asyncio

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

import google.generativeai as genai

dp = Dispatcher()

genai.configure(api_key="AIzaSyDkDI0-Z5SUl8lvRJo077rDoENYYbMGrmU")
model = genai.GenerativeModel('gemini-1.5-flash')

def get_config():
    try:
        with open("config.txt") as f:
            return f.read()
    except Exception as e:
        return ""

CONFIG = get_config()

@dp.message()
async def message(message: Message):
    print(message.text)
    if message.text.startswith("ИИ"):
        await message.reply(model.generate_content(CONFIG + ", вопрос: " + message.text).text, parse_mode="markdown")

async def main():
    bot = Bot(token="7942728169:AAHtm_rDUB1akD01VF0PW5z7jIAyu2G8ur8")

    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Setting up a bot...")
    asyncio.run(main())