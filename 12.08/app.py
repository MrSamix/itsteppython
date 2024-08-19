import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import find_dotenv, load_dotenv
import requests
import os

load_dotenv(find_dotenv())
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Hello {message.from_user.first_name}!")

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("I'am your telegram bot and i help you to make a choice")


@dp.message(Command("sticker"))
async def cmd_hi(message: Message):
    await message.answer_sticker("CAACAgEAAxkBAAEHpS1muh6qsf__32uGkeVZUeUNP_yq6wACwgEAAnY3dj99-AsPaVYkoDUE")

@dp.message(Command("commands"))
async def cmd_commands(message: Message):
    await message.answer("Commands: \n/start - Start the bot \n/help - send a text \n/sticker - send a welcome text \n/commands - send all commands of the bot")

@dp.message(F.text == "Hello")
async def answerhello(message: Message):
    await message.reply(f"Hello, my friend {message.from_user.full_name}")

@dp.message(F.photo)
async def answerphoto(message: Message):
    await message.reply(f"Я отримав від тебе фото!😊")

@dp.message(F.voice)
async def answervoice(message: Message):
    await message.reply(f"Я отримав від тебе голосове повідомлення!😊")

@dp.message(F.sticker)
async def answerasticker(message: Message):
    await message.answer_sticker(message.sticker.file_id)

async def main():
    await dp.start_polling(bot)
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("End of work")