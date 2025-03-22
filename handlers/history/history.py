from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

from handlers.history.hardcode import history_list
from states.states_history import HistoryStates

router = Router()

@router.message(F.data == "🕒 История поиска")
async def start_history(message: types.Message, state: FSMContext):
    await state.set_state(HistoryStates.history)
    await state.update_data(page=0)
    await show_history_page(message, state)


async def show_history_page(message: types.Message, state: FSMContext):
    # TODO запрос в бд на историю поиска в history_list
    data = await state.get_data()
    page = data.get("page", 0)
    start = page * 10
    end = start + 10
    current_history = list(history_list.items())[start:end]

    mes_text = ""
    for song, date in current_history:
        mes_text += f"{date}: {song}\n"

    markup = InlineKeyboardBuilder()
    if page > 0:
        left = types.InlineKeyboardButton(
            text="⬅️ Предыдущие 10",
            callback_data="left"
        )
        markup.add(left)
    if end < len(history_list):
        right = types.InlineKeyboardButton(
            text="➡️ Следующие 10",
            callback_data="right"
        )
        markup.add(right)
    markup.adjust(2)

    # Удаляем предыдущее сообщение, если оно есть
    if "last_message_id" in data:
        await message.bot.delete_message(message.chat.id, data["last_message_id"])

    # Отправляем новое сообщение и сохраняем его ID
    new_message = await message.answer(text=mes_text, reply_markup=markup.as_markup())
    await state.update_data(last_message_id=new_message.message_id)


@router.callback_query(F.data == "left")
async def prev_page(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    page = data.get("page", 0)
    if page > 0:
        await state.update_data(page=page - 1)
        await show_history_page(callback.message, state)
    await callback.answer()


@router.callback_query(F.data == "right")
async def next_page(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    page = data.get("page", 0)
    await state.update_data(page=page + 1)
    await show_history_page(callback.message, state)
    await callback.answer()
