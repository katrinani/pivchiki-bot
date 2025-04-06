# recommendations1.py
import asyncio
import os
import asyncpg
from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, CallbackQuery, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import List
from aiogram.fsm.state import StatesGroup, State
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy.dialects.postgresql import psycopg2


# --- Определение состояний ---
class RecommendationsStates(StatesGroup):
    choose_recommendations = State()
    wait_recommendations = State()
    rate_recommendation = State() # Добавлено состояние для оценки

router = Router()

# --- Конфигурация для подключения к базе данных ---
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "final_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "111")

async def create_db_connection():
    """Создает подключение к базе данных PostgreSQL."""
    try:
        pool = await asyncpg.create_pool(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            min_size=1,
            max_size=20
        )
        return pool
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

async def fetch_tracks(pool: asyncpg.Pool, track_ids: List[int]) -> List[dict]:
    """Получает информацию о треках по их ID."""
    async with pool.acquire() as conn:
        stmt = await conn.prepare("SELECT TrackId, Name, ArtistId, EmotionVector, Song FROM Tracks WHERE TrackId = ANY($1)")
        tracks = await stmt.fetch(track_ids)
        return [dict(track) for track in tracks]

async def get_user_tracks(pool: asyncpg.Pool, user_id: int, num_tracks: int = 5) -> List[int]:
    """Получает последние прослушанные треки пользователя (пример)."""
    async with pool.acquire() as conn:
        stmt = await conn.prepare("SELECT TrackId FROM History WHERE UserId = $1 ORDER BY ListeningDate DESC LIMIT $2")
        records = await stmt.fetch(user_id, num_tracks)
        if records:
            return [record['trackid'] for record in records]
        else:
            # Если история пуста, возвращаем случайные треки (для примера)
            all_tracks_stmt = await conn.prepare("SELECT TrackId FROM Tracks ORDER BY RANDOM() LIMIT $1")
            all_tracks = await all_tracks_stmt.fetch(num_tracks)
            return [track['trackid'] for track in all_tracks]

async def fetch_similar_tracks_by_physical(pool: asyncpg.Pool, track_id: int) -> List[int]:
    """Получает ID физически похожих треков."""
    async with pool.acquire() as conn:
        stmt = await conn.prepare("SELECT PhysicalSimilarTracksIds FROM Tracks WHERE TrackId = $1")
        result = await stmt.fetchrow(track_id)
        if result and result['physicalsimilartracksids']:
            return list(result['physicalsimilartracksids'])
        return []

async def fetch_track_features(pool: asyncpg.Pool, track_id: int):
    """Получает признаки трека."""
    async with pool.acquire() as conn:
        stmt = await conn.prepare("SELECT Features FROM Tracks WHERE TrackId = $1")
        result = await stmt.fetchrow(track_id)
        if result:
            return {"features": result['features']}
        return None

def calculate_similarity(features1, features2):
    """Вычисляет косинусное сходство между двумя векторами признаков."""
    if features1 is None or features2 is None:
        return -1
    dot_product = sum(a * b for a, b in zip(features1, features2))
    magnitude1 = sum(a * a for a in features1) ** 0.5
    magnitude2 = sum(a * a for a in features2) ** 0.5
    if not magnitude1 or not magnitude2:
        return -1
    return dot_product / (magnitude1 * magnitude2)

async def fetch_all_track_features(pool: asyncpg.Pool) -> List[dict]:
    """Получает Features всех треков."""
    async with pool.acquire() as conn:
        stmt = await conn.prepare("SELECT TrackId, Features FROM Tracks")
        records = await stmt.fetch()
        return [dict(record) for record in records]

async def get_recommendations_by_features(pool: asyncpg.Pool, base_track_features: dict, current_track_id: int, num_recommendations: int = 5) -> List[int]:
    """Получает рекомендации на основе Features."""
    all_track_features = await fetch_all_track_features(pool)
    similarities = []
    base_features = base_track_features.get('features')
    if base_features is None:
        return []

    for track_data in all_track_features:
        track_id = track_data['trackid']
        if track_id == current_track_id:
            continue
        track_features = track_data.get('features')
        similarity = calculate_similarity(base_features, track_features)
        if similarity > 0:  # Рассматриваем только положительное сходство
            similarities.append((track_id, similarity))

    similarities.sort(key=lambda item: item[1], reverse=True)
    return [track_id for track_id, _ in similarities[:num_recommendations]]

async def fetch_user_liked_tracks(pool: asyncpg.Pool, user_id: int) -> List[int]:
    """Получает ID треков, которые понравились пользователю (rating = 1)."""
    async with pool.acquire() as conn:
        stmt = await conn.prepare("SELECT TrackId FROM History WHERE UserId = $1 AND rating = 1")
        records = await stmt.fetch(user_id)
        return [record['trackid'] for record in records]

async def fetch_collaboration_similar_tracks(pool: asyncpg.Pool, track_id: int) -> List[int]:
    """Получает ID треков, рекомендованных коллаборативной фильтрацией."""
    async with pool.acquire() as conn:
        stmt = await conn.prepare("SELECT CollaborationSimilarTracksIds FROM Tracks WHERE TrackId = $1")
        result = await stmt.fetchrow(track_id)
        if result and result['collaborationsimilartracksids']:
            return list(result['collaborationsimilartracksids'])
        return []

async def check_collaboration_data_exists(pool: asyncpg.Pool) -> bool:
    """Проверяет, есть ли хотя бы у одного трека данные для коллаборативных рекомендаций."""
    async with pool.acquire() as conn:
        stmt = await conn.prepare("SELECT 1 FROM Tracks WHERE CollaborationSimilarTracksIds IS NOT NULL LIMIT 1")
        result = await stmt.fetchrow()
        return bool(result)

async def perform_collaborative_filtering(pool: asyncpg.Pool):
    """Выполняет расчет коллаборативных рекомендаций и обновляет базу данных."""
    print("Запущен процесс расчета коллаборативных рекомендаций...")
    try:
        async with pool.acquire() as conn:
            # Получение истории прослушиваний
            stmt_history = await conn.prepare("SELECT UserId, TrackId FROM History")
            history_data = await stmt_history.fetch()

            user_track_matrix = {}
            for record in history_data:
                user_id = record['userid']
                track_id = record['trackid']
                if user_id not in user_track_matrix:
                    user_track_matrix[user_id] = {}
                user_track_matrix[user_id][track_id] = 1

            # Получение списка всех TrackId
            stmt_tracks = await conn.prepare("SELECT TrackId FROM Tracks")
            tracks_result = await stmt_tracks.fetch()
            track_ids = [record['trackid'] for record in tracks_result]
            unique_track_ids = sorted(list(set(track_ids)))

            n_users = len(user_track_matrix)
            n_tracks = len(unique_track_ids)

            if n_users == 0 or n_tracks == 0:
                print("Нет данных для выполнения коллаборативной фильтрации.")
                return

            train_matrix = np.zeros((n_users, n_tracks))
            user_list = list(user_track_matrix.keys())

            for i, user_id in enumerate(user_list):
                if user_id in user_track_matrix:
                    for track_id in user_track_matrix[user_id]:
                        if track_id in unique_track_ids:
                            track_index = unique_track_ids.index(track_id)
                            train_matrix[i, track_index] = 1

            # Расчет схожести треков на основе истории прослушиваний
            track_similarity = cosine_similarity(train_matrix.T)

            collab_recommendations = {}
            for i, track_id in enumerate(unique_track_ids):
                # Получаем индексы топ-5 наиболее похожих треков (исключая сам трек)
                similar_track_indices = np.argsort(track_similarity[i])[::-1][1:6]
                similar_tracks = [unique_track_ids[idx] for idx in similar_track_indices]
                collab_recommendations[track_id] = similar_tracks

                # Обновление CollaborationSimilarTracksIds в таблице Tracks
                stmt_update = await conn.prepare("UPDATE Tracks SET CollaborationSimilarTracksIds = $1 WHERE TrackId = $2")
                await stmt_update.fetch(similar_tracks, track_id)

        print("Расчет коллаборативных рекомендаций завершен.")
    except Exception as e:
        print(f"Ошибка при расчете коллаборативных рекомендаций: {e}")

async def rebase_song_from_playlist(pool: asyncpg.Pool, user_id: int, song_name: str, playlist_to_name: str):
    """Функция для добавления песни в плейлист (реализация может отличаться)."""
    # TODO: Реализуйте логику добавления песни в плейлист пользователя
    print(f"Песня '{song_name}' добавлена в плейлист '{playlist_to_name}' пользователя с ID {user_id}.")
    pass

#стартовое окно
@router.message(F.text.endswith("Рекомендации"))
async def start_recommendations(message: types.Message, state: FSMContext):
    markup = InlineKeyboardBuilder()
    by_user = types.InlineKeyboardButton(
        text="👥 От пользователя с похожим вкусом",
        callback_data="user"
    )
    by_mood = types.InlineKeyboardButton(
        text="😊 По настроению",
        callback_data="mood"
    )
    by_choice = types.InlineKeyboardButton(
        text="✨ Основываясь на моем выборе",
        callback_data="based_on_my_choice"
    )

    markup.add(by_mood, by_user, by_choice)
    markup.adjust(2, 2)

    sent_message = await message.answer(text="Выберите тип рекомендации:", reply_markup=markup.as_markup())
    await state.update_data(last_message_id=sent_message.message_id)
    await state.set_state(RecommendationsStates.choose_recommendations)

# От пользователя с похожим вкусом
@router.callback_query(F.data == "user", RecommendationsStates.choose_recommendations)
async def user_recommendations(callback: types.CallbackQuery, state: FSMContext):
    pool = await create_db_connection()
    if not pool:
        await callback.answer("Не удалось подключиться к базе данных.", show_alert=True)
        return

    collaboration_data_exists = await check_collaboration_data_exists(pool)

    if not collaboration_data_exists:
        await callback.message.edit_text(
            "Запускаем процесс анализа пользователей с похожим вкусом. Это может занять некоторое время..."
        )
        await perform_collaborative_filtering(pool)
        collaboration_data_exists = await check_collaboration_data_exists(pool)
        if not collaboration_data_exists:
            await callback.message.edit_text(
                "Не удалось рассчитать рекомендации от пользователей с похожим вкусом."
            )
            await pool.close()
            await callback.answer()
            return
        else:
            await callback.message.edit_text(
                "Анализ пользователей с похожим вкусом завершен. Получаем рекомендации..."
            )

    user_id = callback.from_user.id
    liked_track_ids = await fetch_user_liked_tracks(pool, user_id)
    recommended_track_ids = set()

    for track_id in liked_track_ids:
        similar_tracks = await fetch_collaboration_similar_tracks(pool, track_id)
        recommended_track_ids.update(similar_tracks[:5]) # Берем до 5 рекомендаций от каждого понравившегося трека

    if not recommended_track_ids:
        await callback.message.edit_text("Не удалось найти рекомендации от пользователей с похожим вкусом.")
        await pool.close()
        await callback.answer()
        return

    final_recommendations = await fetch_tracks(pool, list(recommended_track_ids)[:10]) # Получаем информацию о первых 10 рекомендованных треках

    if final_recommendations:
        await display_recommendations(callback, state, "👥 Рекомендации от пользователей с похожим вкусом", final_recommendations)
    else:
        await callback.message.edit_text("Не удалось получить информацию по рекомендованным трекам.")

    await pool.close()
    await callback.answer()

@router.callback_query(F.data == "similar", RecommendationsStates.choose_recommendations)
async def similar_tracks_recommendation(callback: types.CallbackQuery, state: FSMContext):
    pool = await create_db_connection()
    if not pool:
        await callback.answer("Не удалось подключиться к базе данных.", show_alert=True)
        return

    user_id = callback.from_user.id
    base_track_ids = await get_user_tracks(pool, user_id, num_tracks=1) # Берем 1 последний трек для примера
    if not base_track_ids:
        await callback.message.edit_text("Не найдено истории прослушиваний для формирования рекомендаций.")
        await pool.close()
        await callback.answer()
        return

    recommended_track_ids = set()
    for track_id in base_track_ids:
        similar_by_physical = await fetch_similar_tracks_by_physical(pool, track_id)
        if similar_by_physical:
            recommended_track_ids.update(similar_by_physical[:10]) # Берем до 10 физически похожих

    if not recommended_track_ids:
        await callback.message.edit_text("Не удалось найти похожие треки на ваш выбор.")
        await pool.close()
        await callback.answer()
        return

    final_recommendations = await fetch_tracks(pool, list(recommended_track_ids)[:10])
    if final_recommendations:
        await display_recommendations(callback, state, "🎶 Похожие на ваш выбор", final_recommendations)
    else:
        await callback.message.edit_text("Не удалось получить информацию по рекомендованным трекам.")

    await pool.close()
    await callback.answer()

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
    markup.adjust(2, 2)

    mes_text = "Выберите настроение"
    await callback.message.edit_text(text=mes_text, reply_markup=markup.as_markup())
    await state.set_state(RecommendationsStates.choose_recommendations)

async def handle_mood_recommendations(callback: types.CallbackQuery, state: FSMContext, mood: str):
    pool = await create_db_connection()
    if not pool:
        await callback.answer("Не удалось подключиться к базе данных.", show_alert=True)
        return

    # --- TODO: Вставьте сюда логику для получения рекомендаций на основе настроения ---
    # Вам нужно будет использовать столбец EmotionVector из таблицы Tracks
    # и сравнить его с выбранным настроением.
    # Временная заглушка с первыми 10 треками
    async with pool.acquire() as conn:
        stmt = await conn.prepare("SELECT TrackId, Name, Song FROM Tracks LIMIT 10")
        records = await stmt.fetch()
        songs = [{"trackid": rec['trackid'], "name": rec['name'], "song": rec['song']} for rec in records]

    if songs:
        await display_recommendations(callback, state, f"{mood}\n😊 Рекомендации по настроению", songs)
    else:
        await callback.message.edit_text(f"Не удалось найти треки для настроения '{mood}'.")

    await pool.close()
    await callback.answer()

@router.callback_query(F.data == "sad", RecommendationsStates.choose_recommendations)
async def sad_mood(callback: types.CallbackQuery, state: FSMContext):
    await handle_mood_recommendations(callback, state, "Грустное 😢")

@router.callback_query(F.data == "happy", RecommendationsStates.choose_recommendations)
async def happy_mood(callback: types.CallbackQuery, state: FSMContext):
    await handle_mood_recommendations(callback, state, "Веселое 🙂")

@router.callback_query(F.data == "relax", RecommendationsStates.choose_recommendations)
async def relax_mood(callback: types.CallbackQuery, state: FSMContext):
    await handle_mood_recommendations(callback, state, "Спокойное 🥱")

@router.callback_query(F.data == "cheerful", RecommendationsStates.choose_recommendations)
async def cheerful_mood(callback: types.CallbackQuery, state: FSMContext):
    await handle_mood_recommendations(callback, state, "Бодрое 💃")

# Обработчик для кнопки "Основываясь на моем выборе"
@router.callback_query(F.data == "based_on_my_choice", RecommendationsStates.choose_recommendations)
async def recommendations_based_on_choice(callback: types.CallbackQuery, state: FSMContext):
    num_desired_recommendations = 10
    user_id = callback.from_user.id
    pool = await create_db_connection() # Пока оставляем асинхронное подключение для чтения
    if not pool:
        await callback.answer("Не удалось подключиться к базе данных для чтения.", show_alert=True)
        return

    base_track_ids = await get_user_tracks(pool, user_id, num_tracks=5)
    print(f"Получены следующие базовые треки (ID): {base_track_ids}")

    recommended_track_ids = set()

    for track_id in base_track_ids:
        print(f"Обрабатываем трек с ID: {track_id}")
        similar_by_physical = await fetch_similar_tracks_by_physical(pool, track_id)
        print(f"Физически похожие треки (ID): {similar_by_physical}")
        if similar_by_physical:
            recommended_track_ids.update(similar_by_physical[:5])
        else:
            print(f"Нет физически похожих треков для ID: {track_id}. Попытка поиска по признакам.")
            track_features = await fetch_track_features(pool, track_id)
            if track_features and 'features' in track_features:
                recommendations_by_features = await get_recommendations_by_features(pool, track_features, track_id, num_recommendations=10)
                print(f"Рекомендации по признакам (ID): {recommendations_by_features}")
                recommended_track_ids.update(recommendations_by_features)
            else:
                print(f"Не удалось получить признаки для трека с ID: {track_id}")

        print(f"Текущий список рекомендованных треков (ID): {recommended_track_ids}")
        # if len(recommended_track_ids) >= num_desired_recommendations:
        #     break # Достаточно желаемого количества рекомендаций

    print(f"Финальный список рекомендованных треков (ID): {recommended_track_ids}")
    if not recommended_track_ids:
        await callback.message.edit_text("Не удалось найти рекомендации на основе вашего выбора.")
        await pool.close()
        return

    # Получаем полную информацию о рекомендованных треках
    final_recommendations = await fetch_tracks(pool, list(recommended_track_ids)[:num_desired_recommendations])

    if final_recommendations:
        await display_recommendations(callback, state, "✨ Рекомендации, основанные на вашем выборе", final_recommendations)
    else:
        await callback.message.edit_text("Не удалось получить информацию по рекомендованным трекам.")

    await pool.close()
    await callback.answer()

# Обработчик для лайков и дизлайков
@router.callback_query(F.data.startswith("like_"), RecommendationsStates.rate_recommendation)
async def process_like(callback: CallbackQuery, state: FSMContext):
    track_id = int(callback.data.split("_")[1])
    user_id = callback.from_user.id
    pool = await create_db_connection()
    if pool:
        async with pool.acquire() as conn:
            await conn.execute("INSERT INTO History (UserId, TrackId, ListeningDate, rating) VALUES ($1, $2, NOW(), 1) ON CONFLICT (UserId, TrackId) DO UPDATE SET rating = 1, ListeningDate = NOW()", user_id, track_id)
        await pool.close()
        await callback.answer("Спасибо за вашу оценку!")
    else:
        await callback.answer("Не удалось подключиться к базе данных.")

@router.callback_query(F.data.startswith("dislike_"), RecommendationsStates.rate_recommendation)
async def process_dislike(callback: CallbackQuery, state: FSMContext):
    track_id = int(callback.data.split("_")[1])
    user_id = callback.from_user.id
    pool = await create_db_connection()
    if pool:
        async with pool.acquire() as conn:
            await conn.execute("INSERT INTO History (UserId, TrackId, ListeningDate, rating) VALUES ($1, $2, NOW(), -1) ON CONFLICT (UserId, TrackId) DO UPDATE SET rating = -1, ListeningDate = NOW()", user_id, track_id)
        await pool.close()
        await callback.answer("Спасибо за вашу оценку!")
    else:
        await callback.answer("Не удалось подключиться к базе данных.")

# Обработчик для перелистывания страниц и оценки
async def display_recommendations(callback: types.CallbackQuery, state: FSMContext, title: str, tracks: List[dict]):
    await state.update_data(songs=[track['name'] for track in tracks], current_index=0, total=len(tracks), recommended_tracks_data=tracks)
    if tracks:
        track = tracks[0]
        song_path = track.get('song')
        if song_path and os.path.exists(song_path):
            media = types.InputMediaAudio(media=FSInputFile(song_path), caption=title)
            if len(tracks) > 1:
                await callback.bot.edit_message_media(
                    chat_id=callback.message.chat.id,
                    message_id=callback.message.message_id,
                    media=media,
                    reply_markup=await get_pagination_markup(0, len(tracks), state)
                )
            else:
                await callback.bot.edit_message_media(
                    chat_id=callback.message.chat.id,
                    message_id=callback.message.message_id,
                    media=media,
                    reply_markup=None
                )
        else:
            await callback.message.edit_text(f"{title}:\nНе удалось найти аудиофайл для трека '{track['name']}'.")
    else:
        await callback.message.edit_text(f"{title}:\nРекомендации не найдены.")
    await state.set_state(RecommendationsStates.wait_recommendations)

#Обработчик для перелистывания страниц
#Обработчик для перелистывания страниц
@router.callback_query(F.data.in_({"next", "prev"}), RecommendationsStates.wait_recommendations)
async def handle_pagination(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    data = await state.get_data()
    current_index = data.get("current_index", 0)
    total = data.get("total", 0)
    recommended_tracks_data = data.get("recommended_tracks_data")

    if recommended_tracks_data:
        index = current_index
        if callback_query.data == "next":
            index += 1
        elif callback_query.data == "prev":
            index -= 1

        if 0 <= index < total:
            await state.update_data(current_index=index)
            track = recommended_tracks_data[index]
            song_path = track.get('song')
            track_name = track.get('name')
            title = f"Рекомендация: {track_name}"

            try:
                if song_path and os.path.exists(song_path):
                    media = types.InputMediaAudio(media=FSInputFile(song_path), caption=title)
                    await callback_query.bot.edit_message_media(
                        chat_id=user_id,
                        message_id=callback_query.message.message_id,
                        media=media,
                        reply_markup=await get_pagination_markup(index, total, state)
                    )
                    await callback_query.answer()
                else:
                    await callback_query.answer("Аудиофайл не найден.", show_alert=True)
            except Exception as e:
                import logging
                logging.error(f"Ошибка при обновлении аудио: {e}")
                await callback_query.answer("Произошла ошибка при обновлении аудио.", show_alert=True)
        else:
            await callback_query.answer("Нет больше треков.", show_alert=True)
    else:
        await callback_query.answer("Нет доступных рекомендаций.", show_alert=True)

#клавиатура для перелистывания и оценивания
async def get_pagination_markup(current_index: int, total: int, state: FSMContext):
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
    recommended_tracks_data = None
    try:
        state_data = await state.get_data()
        recommended_tracks_data = state_data.get("recommended_tracks_data")
        track_id = recommended_tracks_data[current_index]['trackid'] if recommended_tracks_data else None
        builder.row(
            InlineKeyboardButton(text="👍", callback_data=f"like_{track_id}" if track_id else "like_none"),
            InlineKeyboardButton(text="👎", callback_data=f"dislike_{track_id}" if track_id else "dislike_none")
        )
    except Exception as e:
        print(f"Ошибка при создании кнопок оценки: {e}")
        builder.row(
            InlineKeyboardButton(text="👍", callback_data="like_none"),
            InlineKeyboardButton(text="👎", callback_data="dislike_none")
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
@router.callback_query(F.data == "add_to_playlist", RecommendationsStates.wait_recommendations)
async def handle_playlist(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    current_index = data["current_index"]
    songs = data["songs"]
    recommended_tracks_data = data["recommended_tracks_data"]
    selected_song_name = songs[current_index]
    user_id = callback.from_user.id
    pool = await create_db_connection()
    if pool:
        await rebase_song_from_playlist(pool, user_id, selected_song_name, "Избранное")
        await pool.close()
        await callback.answer(
            text=f"«{selected_song_name}» добавлена в плейлист Избранное!",
            show_alert=False
        )
    else:
        await callback.answer("Не удалось подключиться к базе данных.")


#обработчик лайков и дизлайков
@router.callback_query(F.data.in_({"like_none", "dislike_none"}), RecommendationsStates.wait_recommendations)
async def handle_reaction_none(callback: types.CallbackQuery):
    await callback.answer("Не удалось получить ID трека для оценки.", show_alert=True)

@router.callback_query(F.data.in_({"like", "dislike"}))
async def handle_reaction(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    current_index = data["current_index"]
    songs = data["songs"]
    selected_song = songs[current_index]
    user_id = callback.from_user.id
    track_id = None
    recommended_tracks_data = data.get("recommended_tracks_data")
    if recommended_tracks_data and current_index < len(recommended_tracks_data):
        track_id = recommended_tracks_data[current_index]['trackid']

    if track_id is None:
        await callback.answer("Не удалось получить ID трека для оценки.", show_alert=True)
        return

    rating = 1 if callback.data == "like" else -1

    pool = await create_db_connection()
    if not pool:
        await callback.answer("Не удалось подключиться к базе данных.", show_alert=True)
        return

    async with pool.acquire() as conn:
        # Проверяем, существует ли уже запись для данного пользователя и трека
        stmt_check = await conn.prepare("SELECT 1 FROM History WHERE UserId = $1 AND TrackId = $2")
        existing_record = await stmt_check.fetchrow(user_id, track_id)

        if existing_record:
            # Если запись существует, обновляем ее
            stmt_update = await conn.prepare("UPDATE History SET rating = $3, ListeningDate = NOW() WHERE UserId = $1 AND TrackId = $2")
            await stmt_update.execute(user_id, track_id, rating)
        else:
            # Если запись не существует, создаем новую
            stmt_insert = await conn.prepare("INSERT INTO History (UserId, TrackId, ListeningDate, rating) VALUES ($1, $2, NOW(), $3)")
            await stmt_insert.execute(user_id, track_id, rating)

    reaction = "лайкнута" if callback.data == "like" else "дизлайкнута"
    await callback.answer(f"Песня «{selected_song}» {reaction}!", show_alert=False)
    await pool.close()

# Обработчик для кнопки "Основываясь на моем выборе"
@router.callback_query(F.data == "based_on_my_choice", RecommendationsStates.choose_recommendations)
async def recommendations_based_on_choice(callback: types.CallbackQuery, state: FSMContext):
    num_desired_recommendations = 10
    user_id = callback.from_user.id
    pool = await create_db_connection() # Пока оставляем асинхронное подключение для чтения
    if not pool:
        await callback.answer("Не удалось подключиться к базе данных для чтения.", show_alert=True)
        return

    base_track_ids = await get_user_tracks(pool, user_id, num_tracks=5)
    print(f"Получены следующие базовые треки (ID): {base_track_ids}")

    recommended_track_ids = set()

    for track_id in base_track_ids:
        print(f"Обрабатываем трек с ID: {track_id}")
        similar_by_physical = await fetch_similar_tracks_by_physical(pool, track_id)
        print(f"Физически похожие треки (ID): {similar_by_physical}")
        if similar_by_physical:
            recommended_track_ids.update(similar_by_physical[:5])
        else:
            print(f"Нет физически похожих треков для ID: {track_id}. Попытка поиска по признакам.")
            track_features = await fetch_track_features(pool, track_id)
            if track_features and 'features' in track_features:
                recommendations_by_features = await get_recommendations_by_features(pool, track_features, track_id, num_recommendations=10)
                print(f"Рекомендации по признакам (ID): {recommendations_by_features}")
                recommended_track_ids.update(recommendations_by_features)
            else:
                print(f"Не удалось получить признаки для трека с ID: {track_id}")

        print(f"Текущий список рекомендованных треков (ID): {recommended_track_ids}")
        # if len(recommended_track_ids) >= num_desired_recommendations:
        #     break # Достаточно желаемого количества рекомендаций

    print(f"Финальный список рекомендованных треков (ID): {recommended_track_ids}")
    if not recommended_track_ids:
        await callback.message.edit_text("Не удалось найти рекомендации на основе вашего выбора.")
        await pool.close()
        return

    # Получаем полную информацию о рекомендованных треках
    final_recommendations = await fetch_tracks(pool, list(recommended_track_ids)[:num_desired_recommendations])

    if final_recommendations:
        await display_recommendations(callback, state, "✨ Рекомендации, основанные на вашем выборе", final_recommendations)
    else:
        await callback.message.edit_text("Не удалось получить информацию по рекомендованным трекам.")

    await pool.close()
    await callback.answer()