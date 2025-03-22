from aiogram import types, Router
from aiogram.filters import Command

router = Router()

@router.message(Command('start'))
async def start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="🕒 История поиска")],
        [types.KeyboardButton(text="🎵 Поиск музыки")],
        [types.KeyboardButton(text="⬆️ Загрузить трек")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

    await message.answer(text="Привет, это первое сообщение", reply_markup=keyboard)
