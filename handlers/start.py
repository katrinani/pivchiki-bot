from aiogram import types, Router
from aiogram.filters import Command

from sources.postgres.sql_requests import create_user

router = Router()

@router.message(Command('start'))
async def start(message: types.Message):
    user_id = message.from_user.id
    ok = create_user(user_id)
    if not ok:
        await message.answer("Что-то пошло не так, поробуйте снова")
        return


    kb = [
        [types.KeyboardButton(text="🕒 История поиска")],
        [types.KeyboardButton(text="🎵 Поиск музыки")],
        [types.KeyboardButton(text="⬆️ Загрузить трек")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

    await message.answer(text="Привет, это первое сообщение", reply_markup=keyboard)
