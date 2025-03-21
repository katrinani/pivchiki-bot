from aiogram import F, types, Router
from aiogram.filters import Command

router = Router()

@router.message(Command('start'))
async def start(message: types.Message):
    await message.answer(text="Привет, это первое сообщение")
