from aiogram import F, types, Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from states.states_recommendations import RecommendationsStates

router = Router()

#стартовое окно
@router.message(F.text.endswith("Рекомендации"))
async def start_recommendations(message: types.Message, state: FSMContext):

    markup = InlineKeyboardBuilder()
    by_user = types.InlineKeyboardButton(
        text="👥 От пользователя с похожим вкусом",
        callback_data="user"
    )
    by_similar = types.InlineKeyboardButton(
        text="🎶 Похожие на ваш выбор",
        callback_data="similar"
    )
    by_mood = types.InlineKeyboardButton(
        text="😊 По настроению",
        callback_data="mood"
    )

    markup.add(by_mood, by_user, by_similar)
    markup.adjust(1, 1)

    sent_message = await message.answer(text="Выберите тип рекомендации:", reply_markup=markup.as_markup())
    await state.update_data(last_message_id=sent_message.message_id)
    await state.set_state(RecommendationsStates.choose_recommendations)


# От пользователя с похожим вкусом
@router.callback_query(F.data == "user", RecommendationsStates.choose_recommendations)
async def sad_mood(callback: types.CallbackQuery, state: FSMContext):
    # TODO запрос к алгоритму похожий пользователь
    songs = ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5",
             "Song 6", "Song 7", "Song 8", "Song 9", "Song 10"]

    await state.update_data(
        songs=songs,
        current_index=0,
        total=len(songs)
    )

    await callback.message.edit_text(
        text=f"👥 От пользователя с похожим вкусом:\n🎵 {songs[0]}",
        reply_markup=get_pagination_markup(0, len(songs))
    )
    await state.set_state(RecommendationsStates.wait_recommendations)


@router.callback_query(F.data == "similar", RecommendationsStates.choose_recommendations)
async def sad_mood(callback: types.CallbackQuery, state: FSMContext):
    # TODO запрос к алгоритму похожий плейлсит на ваш
    songs = ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5",
             "Song 6", "Song 7", "Song 8", "Song 9", "Song 10"]

    await state.update_data(
        songs=songs,
        current_index=0,
        total=len(songs)
    )

    await callback.message.edit_text(
        text=f"🎶 Похожие на ваш выбор:\n🎵 {songs[0]}",
        reply_markup=get_pagination_markup(0, len(songs))
    )
    await state.set_state(RecommendationsStates.wait_recommendations)


#По настроению
@router.callback_query(F.data == "mood", RecommendationsStates.choose_recommendations)
async def choose_mood(callback: types.CallbackQuery, state: FSMContext):
    markup = InlineKeyboardBuilder()
    by_sad = types.InlineKeyboardButton(
        text="Грустное 😢",
        callback_data="sad"
    )
    by_happy = types.InlineKeyboardButton(
        text="Веселое 🙂",
        callback_data="happy"
    )
    by_relax = types.InlineKeyboardButton(
        text="Спокойное 🥱",
        callback_data="relax"
    )
    by_cheerful = types.InlineKeyboardButton(
        text="Бодрое 💃",
        callback_data="cheerful"
    )

    markup.add(by_happy, by_sad, by_relax, by_cheerful)
    markup.adjust(1, 1, 1, 1)

    mes_text = "Выберите настроение"
    await callback.message.edit_text(text=mes_text, reply_markup=markup.as_markup())
    await state.set_state(RecommendationsStates.choose_recommendations)


@router.callback_query(F.data == "sad", RecommendationsStates.choose_recommendations)
async def sad_mood(callback: types.CallbackQuery, state: FSMContext):
    # TODO запрос к алгоритму по настроению "Грустное"
    songs = ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5",
             "Song 6", "Song 7", "Song 8", "Song 9", "Song 10"]

    await state.update_data(
        songs=songs,
        current_index=0,
        total=len(songs)
    )

    await callback.message.edit_text(
        text=f"Грустное 😢\n🎵 {songs[0]}",
        reply_markup=get_pagination_markup(0, len(songs))
    )
    await state.set_state(RecommendationsStates.wait_recommendations)


@router.callback_query(F.data == "happy", RecommendationsStates.choose_recommendations)
async def happy_mood(callback: types.CallbackQuery, state: FSMContext):
    # TODO запрос к алгоритму по настроению "Веселое"
    songs = ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5",
             "Song 6", "Song 7", "Song 8", "Song 9", "Song 10"]

    await state.update_data(
        songs=songs,
        current_index=0,
        total=len(songs)
    )

    await callback.message.edit_text(
        text=f"Веселое 🙂\n🎵 {songs[0]}",
        reply_markup=get_pagination_markup(0, len(songs))
    )
    await state.set_state(RecommendationsStates.wait_recommendations)

@router.callback_query(F.data == "relax", RecommendationsStates.choose_recommendations)
async def relax_mood(callback: types.CallbackQuery, state: FSMContext):
    #TODO запрос к алгоритму по настроению "Споконое"
    songs = ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5",
             "Song 6", "Song 7", "Song 8", "Song 9", "Song 10"]

    await state.update_data(
        songs=songs,
        current_index=0,
        total=len(songs)
    )

    await callback.message.edit_text(
        text=f"Спокойное 🥱\n🎵 {songs[0]}",
        reply_markup=get_pagination_markup(0, len(songs))
    )
    await state.set_state(RecommendationsStates.wait_recommendations)


@router.callback_query(F.data == "cheerful", RecommendationsStates.choose_recommendations)
async def cheerful_mood(callback: types.CallbackQuery, state: FSMContext):
    # TODO запрос к алгоритму по настроению "Бодроее"
    songs = ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5",
             "Song 6", "Song 7", "Song 8", "Song 9", "Song 10"]

    await state.update_data(
        songs=songs,
        current_index=0,
        total=len(songs)
    )

    await callback.message.edit_text(
        text=f"Бодрое 💃\n🎵 {songs[0]}",
        reply_markup=get_pagination_markup(0, len(songs))
    )
    await state.set_state(RecommendationsStates.wait_recommendations)



#Обработчик для перелистывания страниц
@router.callback_query(F.data.in_({"next", "prev"}))
async def handle_pagination(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    current_index = data["current_index"]
    total = data["total"]
    songs = data["songs"]

    if callback.data == "next" and current_index < total - 1:
        current_index += 1
    elif callback.data == "prev" and current_index > 0:
        current_index -= 1

    await state.update_data(current_index=current_index)

    await callback.message.edit_text(
        text=f"🎵 {songs[current_index]}",
        reply_markup=get_pagination_markup(current_index, total)
    )
    await callback.answer()

#клавиатура для перелистывания и оценивания
def get_pagination_markup(current_index: int, total: int):
    builder = InlineKeyboardBuilder()

    # Строка пагинации
    pagination_buttons = []
    if current_index > 0:
        pagination_buttons.append(InlineKeyboardButton(text="⬅️", callback_data="prev"))
    pagination_buttons.append(InlineKeyboardButton(text=f"{current_index + 1}/{total}", callback_data="ignore"))
    if current_index < total - 1:
        pagination_buttons.append(InlineKeyboardButton(text="➡️", callback_data="next"))
    builder.row(*pagination_buttons)

    # Строка реакций
    builder.row(
        InlineKeyboardButton(text="👍", callback_data="like"),
        InlineKeyboardButton(text="👎", callback_data="dislike")
    )

    # Строка плейлиста
    builder.row(
        InlineKeyboardButton(
            text="Добавить в плейлист",
            callback_data="add_to_playlist"
        )
    )

    return builder.as_markup()

#Добавление в плейлист
@router.callback_query(F.data == "add_to_playlist")
async def handle_playlist(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    current_index = data["current_index"]
    songs = data["songs"]
    selected_song = songs[current_index]

    #TODO сделать запрос к БД для добавление песни в плейлист

    await callback.answer(
        text=f"«{selected_song}» добавлена в ваш плейлист!",
        show_alert=False
    )


#обработчик лайков и дизлайков
@router.callback_query(F.data.in_({"like", "dislike"}))
async def handle_reaction(callback: types.CallbackQuery):
    #TODO сделать запрос к БД который будет добавлять песню в плейлист
    reaction = "лайкнута" if callback.data == "like" else "дизлайкнута"
    await callback.answer(f"Песня {reaction}!", show_alert=False)




