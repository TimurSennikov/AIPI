import asyncio

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import *

import aiogram.filters
import aiogram.types

import google.generativeai as genai

import PIL.Image

import os

dp = Dispatcher()
bot = Bot(token="TG_BOT_TOKEN")

genai.configure(api_key="GEMINI_API_TOKEN")
model = genai.GenerativeModel('gemini-1.5-pro')

def get_config():
    try:
        with open("config.txt") as f:
            return f.read()
    except Exception as e:
        return ""

CONFIG = get_config()

@dp.message()
async def message(message: aiogram.types.Message):
    if message.content_type == aiogram.types.ContentType.TEXT:
        await message.reply(model.generate_content(CONFIG + ", вопрос: " + message.text).text, parse_mode="markdown")
    elif message.content_type == aiogram.types.ContentType.PHOTO:
        t = []

        if(message.caption != None):
            t.append(message.caption)

        if not os.path.exists("photos/"):
            os.mkdir("photos")

        for photo in message.photo:
            await bot.download(photo, "photos/" + photo.file_id + ".png")
            img = PIL.Image.open("photos/" + photo.file_id + ".png")
            t.append(img)

        await message.reply(model.generate_content(t).text)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Setting up a bot...")
    asyncio.run(main())