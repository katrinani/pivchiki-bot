from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

from states.states_history import HistoryStates
from sources.postgres.sql_requests import get_history

router = Router()


@router.message(F.text.endswith("История поиска"))
async def start_history(message: types.Message, state: FSMContext):
    await state.set_state(HistoryStates.history)
    await state.update_data(page=0)
    await show_history_page(message, state)


async def show_history_page(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    history_list = get_history(user_id)

    data = await state.get_data()
    page = data.get("page", 0)
    items_per_page = 10
    start = page * items_per_page
    end = start + items_per_page
    current_history = history_list[start:end]

    mes_text = "Ваша история прослушиваний:\n\n"
    for idx, item in enumerate(current_history, start=1):
        mes_text += (
            f"{idx + start}. {item['song']}"
            f"   🗓 {item['date']}\n\n"
        )

    total_pages = (len(history_list) + items_per_page - 1) // items_per_page
    mes_text += f"Страница {page + 1} из {total_pages}"

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

    # Редактируем существующее сообщение, если оно есть
    if "last_message_id" in data:
        await message.bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=data["last_message_id"],
            text=mes_text,
            reply_markup=markup.as_markup()
        )
    else:
        # Если сообщения нет, отправляем новое и сохраняем его ID
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