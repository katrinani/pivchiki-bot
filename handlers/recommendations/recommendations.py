from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

from sources.recomendations.collaboration_recomendation import main_get_recommendations
from states.states_recommendations import RecommendationsStates
from sources.postgres.sql_requests import rebase_song_from_playlist, get_track_id, rating_process, get_track_name, \
    get_track_path
from sources.recomendations.text_grade import get_similar_tracks
from sources.recomendations.physic_grade import get_similar_features
from sources.postgres.sql_requests import get_best_tracks
from sources.postgres.sql_requests import get_best_features

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

    markup.add(by_user, by_similar, by_mood)
    markup.adjust(1, 1)

    sent_message = await message.answer(text="Выберите тип рекомендации:", reply_markup=markup.as_markup())
    await state.update_data(last_message_id=sent_message.message_id)
    await state.set_state(RecommendationsStates.choose_recommendations)

# От пользователя с похожим вкусом
@router.callback_query(F.data == "user", RecommendationsStates.choose_recommendations)
async def recommend_by_similar_user(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    recommended_tracks_data = main_get_recommendations(user_id)

    if recommended_tracks_data:
        tracks_id = [id.split("trackid")[1] for id, prediction in recommended_tracks_data]

        songs = []
        paths =[]
        for id in tracks_id:
            songs.append(get_track_name(id))
            paths.append(get_track_path(id))


        await state.update_data(
            songs=songs,
            paths=paths,
            current_index=0,
            total=len(songs),
            last_message_id=None
        )

        # Отправляем первое аудио
        file = FSInputFile(paths[0][0])
        message = await callback.message.answer_audio(
            file,
            caption=f"\n🎵 {songs[0][0]}",
            reply_markup=get_pagination_markup(0, len(songs))
        )

        # Сохраняем ID сообщения
        await state.update_data(last_message_id=message.message_id)

        # Удаляем исходное сообщение с кнопкой
        await callback.message.delete()

        await state.set_state(RecommendationsStates.wait_recommendations)
    else:
        await callback.message.edit_text(
            text="Нет рекомендаций от пользователей с похожим вкусом."
        )

@router.callback_query(F.data == "similar", RecommendationsStates.choose_recommendations)
async def sad_mood(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id

    # Используем ID пользователя для получения треков
    songs, paths = get_similar_features(get_best_features(str(user_id))[-5:])

    await state.update_data(
        songs=songs,
        paths=paths,
        current_index=0,
        total=len(songs),
        last_message_id=None
    )

    # Отправляем первое аудио
    file = FSInputFile(paths[0])
    message = await callback.message.answer_audio(
        file,
        caption=f"\n🎵 {songs[0]}",
        reply_markup=get_pagination_markup(0, len(songs))
    )

    # Сохраняем ID сообщения
    await state.update_data(last_message_id=message.message_id)

    # Удаляем исходное сообщение с кнопкой
    await callback.message.delete()

    await state.set_state(RecommendationsStates.choose_recommendations)


#По настроению
@router.callback_query(F.data == "mood", RecommendationsStates.choose_recommendations)
async def choose_mood(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id

    # Используем ID пользователя для получения треков
    songs, paths = get_similar_tracks(get_best_tracks(str(user_id))[-5:])

    await state.update_data(
        songs=songs,
        paths=paths,
        current_index=0,
        total=len(songs),
        last_message_id=None
    )

    # Отправляем первое аудио
    file = FSInputFile(paths[0])
    message = await callback.message.answer_audio(
        file,
        caption=f"\n🎵 {songs[0]}",
        reply_markup=get_pagination_markup(0, len(songs))
    )

    # Сохраняем ID сообщения
    await state.update_data(last_message_id=message.message_id)

    # Удаляем исходное сообщение с кнопкой
    await callback.message.delete()

    await state.set_state(RecommendationsStates.choose_recommendations)


@router.callback_query(F.data.in_({"next", "prev"}))
async def handle_pagination(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    current_index = data["current_index"]
    total = data["total"]
    songs = data["songs"]
    paths = data["paths"]
    last_message_id = data.get("last_message_id")

    # Определяем новый индекс
    new_index = current_index
    if callback.data == "next" and current_index < total - 1:
        new_index += 1
    elif callback.data == "prev" and current_index > 0:
        new_index -= 1

    if new_index == current_index:
        await callback.answer()
        return

    # 1. Сначала отправляем новое аудио
    file = FSInputFile(paths[new_index][0])
    try:
        message = await callback.message.answer_audio(
            audio=file,
            caption=f"🎵 {songs[new_index][0]}",
            reply_markup=get_pagination_markup(new_index, total)
        )
    except Exception as e:
        await callback.answer("Ошибка при загрузке трека", show_alert=True)
        return

    # 2. Только после успешной отправки удаляем старое сообщение
    if last_message_id:
        try:
            await callback.bot.delete_message(
                chat_id=callback.message.chat.id,
                message_id=last_message_id
            )
        except:
            pass  # Если не удалось удалить, не прерываем работу

    # 3. Обновляем состояние
    await state.update_data(
        current_index=new_index,
        last_message_id=message.message_id
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

    # сохранение в БД (код может отличаться в зависимости от вашей реализации)
    rebase_song_from_playlist(callback.message.from_user.id,song_name=selected_song, playlist_to_name="Избранное")

    await callback.answer(
        text=f"«{selected_song}» добавлена в плейлист Избранное!",
        show_alert=False
    )


#обработчик лайков и дизлайков
@router.callback_query(F.data.in_({"like", "dislike"}))
async def handle_reaction(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    current_index = data["current_index"]
    songs = data["songs"]
    selected_song = songs[current_index]
    trackid = get_track_id(selected_song)
    reaction_str = "лайк" if callback.data =="like" else "дизлайк"

    reaction_value = 1 if callback.data == "like" else -1
    user_id = callback.from_user.id
    ok = rating_process(user_id, trackid, reaction_value)
    if ok:
        await callback.message.answer(f"Вы поставили {reaction_str}")
    else:
        await callback.message.answer("Что-то пошло не так.")
