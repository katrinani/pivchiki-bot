from aiogram import types, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.message(Command('start'))
async def start(message: types.Message):
    # TODO убрать хардкод
    markup = InlineKeyboardBuilder()
    search = types.InlineKeyboardButton(
        text="f",
        callback_data="search"
    )
    markup.add(search)
    await message.answer(text="Привет, это первое сообщение", reply_markup=markup.as_markup())
