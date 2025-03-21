from asyncio import run
from aiogram import Bot, Dispatcher

from handlers import start
from handlers.search import search

TOKEN = "7258847191:AAGCd4xDlAM4MjDlnGBfHtEmUNTU19Xc7E8"

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    # создаем роутеры в тех файлах где мы работаем и вызываем функции здесь
    dp.include_router(start.router)
    dp.include_router(search.router)
    #  dp.include_router(файл.router)


    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main())