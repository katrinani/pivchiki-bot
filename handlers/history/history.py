from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from states.states_history import HistoryStates
from sources.postgres.sql_requests import get_history

router = Router()


@router.message(F.text.endswith("История поиска"))
async def start_history(message: types.Message, state: FSMContext):
    history_data = get_history(message.from_user.id)
    await state.set_state(HistoryStates.history)
    await state.update_data(
        history=history_data,
        page=0,
        total_items=len(history_data),
        last_message_id=None
    )
    await show_history_page(message, state)


async def show_history_page(message: types.Message, state: FSMContext):
    data = await state.get_data()
    history_list = data.get("history", [])
    page = data.get("page", 0)
    items_per_page = 10
    total_items = len(history_list)

    # Корректировка номера страницы
    total_pages = max((total_items - 1) // items_per_page + 1, 1)
    current_page = min(max(page, 0), total_pages - 1)

    if current_page != page:
        await state.update_data(page=current_page)

    start = current_page * items_per_page
    end = start + items_per_page
    current_history = history_list[start:end]

    # Формирование текста
    mes_text = "Ваша история прослушиваний:\n\n" if total_items > 0 else "История пуста\n"
    for idx, item in enumerate(current_history, start=start + 1):
        mes_text += (
            f"{idx}. {item['song']}\n"
            f"   🗓 {item['date']}\n\n"
        )

    if total_items > 0:
        mes_text += f"Страница {current_page + 1} из {total_pages}"

    # Создание клавиатуры
    markup = InlineKeyboardBuilder()
    if current_page > 0:
        markup.button(text="⬅️ Назад", callback_data="prev_page")
    if end < total_items:
        markup.button(text="Вперед ➡️", callback_data="next_page")
    markup.adjust(2)

    # Обновление сообщения
    try:
        if data.get("last_message_id"):
            await message.bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=data["last_message_id"],
                text=mes_text,
                reply_markup=markup.as_markup()
            )
        else:
            new_message = await message.answer(mes_text, reply_markup=markup.as_markup())
            await state.update_data(last_message_id=new_message.message_id)
    except Exception as e:
        print(f"Error updating message: {e}")


@router.callback_query(F.data.in_(["prev_page", "next_page"]))
async def handle_pagination(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    current_page = data.get("page", 0)
    items_per_page = 10
    total_pages = max((len(data.get("history", [])) - 1) // items_per_page + 1, 1)

    if callback.data == "prev_page" and current_page > 0:
        new_page = current_page - 1
    elif callback.data == "next_page" and current_page < total_pages - 1:
        new_page = current_page + 1
    else:
        await callback.answer()
        return

    await state.update_data(page=new_page)
    await show_history_page(callback.message, state)
    await callback.answer()
