from asyncio import run
from aiogram import Bot, types, Dispatcher
from aiogram.filters import Command

TOKEN = "7258847191:AAGCd4xDlAM4MjDlnGBfHtEmUNTU19Xc7E8"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def choice_of_area(message: types.Message):
    await message.answer(text="Привет, это первое сообщение")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    run(main())