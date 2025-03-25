from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from pyexpat.errors import messages
from wsproto.events import Message

from states.states_playlists import PlaylistsStates
from states.states_recommendations import RecommendationsStates

router = Router()

playlists = {"playlist 1" : ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5"],
                  "playlist 2": ["Song 6", "Song 7", "Song 8", "Song 9", "Song 10"],
                  "playlist 3": ["Song 11", "Song 12", "Song 13", "Song 14", "Song 15"]}


#стартовое окно
@router.message(F.text.endswith("Мои плейлисты"))
async def start_recommendations(message: types.Message, state: FSMContext):
    markup = InlineKeyboardBuilder()

    for name in playlists.keys():
        markup.add(types.InlineKeyboardButton(text = str(name), callback_data= str(name)))
    markup.adjust(1, 1)

    sent_message = await message.answer(text="Ваши плейлисты:", reply_markup=markup.as_markup())
    await state.update_data(last_message_id=sent_message.message_id)
    await state.set_state(PlaylistsStates.choose_playlist)


@router.callback_query(PlaylistsStates.choose_playlist)
async def playlist_menu(callback: types.CallbackQuery, state: FSMContext):
    name_playlist = callback.data
    await state.update_data(name_playlist=name_playlist)
    markup = InlineKeyboardBuilder()
    listen = types.InlineKeyboardButton(
        text="🎧 Прослушать плейлист",
        callback_data="listen"
    )
    edit = types.InlineKeyboardButton(
        text="✏️ Редактировать плейлист",
        callback_data="edit"
    )
    create = types.InlineKeyboardButton(
        text="➕ Создать плейлист",
        callback_data="create"
    )
    markup.add(listen, edit, create )
    markup.adjust(1, 1)

    songs = ""
    count = 0
    for name in playlists[name_playlist]:
        count += 1
        songs += f"\n{count}: {name}"
    await callback.message.edit_text(text=f"{songs}", reply_markup=markup.as_markup())
    await state.set_state(PlaylistsStates.choose_action)

#редактирование
@router.callback_query(F.data == "edit", PlaylistsStates.choose_action)
async def edit_menu(callback: types.CallbackQuery, state: FSMContext):
    markup = InlineKeyboardBuilder()
    rename = types.InlineKeyboardButton(
        text="✏️ Изменить название",
        callback_data="rename"
    )
    delete = types.InlineKeyboardButton(
        text="🗑️ Удалить плейлист",
        callback_data="delete"
    )
    edit_songs = types.InlineKeyboardButton(
        text="🎵 Редактировать песни",
        callback_data="edit_songs"
    )
    markup.add(rename, edit_songs, delete)
    markup.adjust(1, 1)
    await callback.message.edit_text(text="Выбирете функцию", reply_markup=markup.as_markup())
    await state.set_state(PlaylistsStates.wait_choose)

#переименование
@router.callback_query(F.data == "rename", PlaylistsStates.wait_choose)
async def rename(callback: types.CallbackQuery, state: FSMContext):
    mes_text = "Напишите новое название плейлиста"
    await callback.message.edit_text(text=mes_text)
    await state.set_state(PlaylistsStates.rename)

@router.message(F.text, PlaylistsStates.rename)
async def rename(message: types.Message, state: FSMContext):
    data = await state.get_data()
    try:
        playlists[message.text] = playlists.pop(str(data['name_playlist']))
    except KeyError:
        await message.answer(text="Такого плейлиста нет")
    mes_text = f"Плейлист переименован на {message.text}"
    await message.answer(text=mes_text)
    await state.set_state(PlaylistsStates.action)


#удаление
@router.callback_query(F.data == "delete", PlaylistsStates.wait_choose)
async def rename(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    mes_text = f"Плейлист {data['name_playlist']} удален"
    try:
        playlists.pop(str(data['name_playlist']))
    except KeyError:
        await callback.message.edit_text(text="Такого плейлиста нет")
    await callback.message.edit_text(text=mes_text)
    await state.set_state(PlaylistsStates.action)


#редактрование песен
@router.callback_query(F.data == "edit_songs", PlaylistsStates.wait_choose)
async def rename(callback: types.CallbackQuery, state: FSMContext):
    mes_text = "Напишите индекс(ы) песни(песен) для удаления ЧЕРЕЗ ЗАПЯТУЮ"
    await callback.message.edit_text(text=mes_text)
    await state.set_state(PlaylistsStates.edit_songs)


@router.message(F.text, PlaylistsStates.edit_songs)
async def rename(message: types.Message, state: FSMContext):
    data = await state.get_data()
    indexes = message.text.split(",")
    try:
        # Сортируем индексы в обратном порядке
        for i in sorted(indexes, reverse=True):
            if 0 <= int(i) < len(playlists[data['name_playlist']]):
                del playlists[data['name_playlist']][int(i) - 1]
    except Exception as e:
        await message.answer(text=f"Ошибка:{e}")
        return

    mes_text = f"Песня(и) удалена(ы)"
    await message.answer(text=mes_text)
    await state.set_state(PlaylistsStates.action)


#функция удаления
def safe_delete_elements(original: list, indexes: list) -> list:
    """Безопасное удаление элементов по индексам с валидацией"""
    if not isinstance(original, list):
        raise TypeError(f"Ожидается список, получен {type(original).__name__}")

    if not isinstance(indexes, (list, tuple, set)):
        raise TypeError(f"Индексы должны быть коллекцией, получен {type(indexes).__name__}")

    # Фильтрация и нормализация индексов
    valid_indexes = []
    for idx in set(indexes):  # Удаляем дубликаты
        if not isinstance(idx, int):
            print(f"Пропуск нецелочисленного индекса: {idx} ({type(idx).__name__})")
            continue

        # Обработка отрицательных индексов
        normalized_idx = idx if idx >=0 else len(original) + idx

        if 0 <= normalized_idx < len(original):
            valid_indexes.append(normalized_idx)
        else:
            print(f"Пропуск невалидного индекса: {idx} (допустимый диапазон: 0-{len(original)-1})")

    # Сортировка в обратном порядке для безопасного удаления
    for i in sorted(valid_indexes, reverse=True):
        del original[i]

    return original


#создание плейлиста
@router.callback_query(F.data == "create", PlaylistsStates.choose_action)
async def rename(callback: types.CallbackQuery, state: FSMContext):
    mes_text = "Напишите название плейлиста"
    await callback.message.edit_text(text=mes_text)

    await state.set_state(PlaylistsStates.create_playlist)

@router.message(F.text, PlaylistsStates.create_playlist)
async def rename(message: types.Message, state: FSMContext):
    text = message.text
    if text not in playlists:
        playlists[text] = []
    else:
        await message.answer(text="Такой плейлист уже существует")
        return
    mes_text = f"Плейлист {message.text} создан"
    await message.answer(text=mes_text)
    await state.set_state(PlaylistsStates.action)




#прослушивание песен
@router.callback_query(F.data == "listen", PlaylistsStates.choose_action)
async def listen_menu(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    markup = InlineKeyboardBuilder()
    sequential = types.InlineKeyboardButton(
        text="▶️ По порядку",
        callback_data="sequential"
    )
    shuffle = types.InlineKeyboardButton(
        text="🔀 Перемешать",
        callback_data="shuffle"
    )
    markup.add(shuffle, sequential)
    markup.adjust(1, 1)

    songs = ""
    for song in playlists[data['name_playlist']]:
        songs += f"\n{song}"
    await callback.message.edit_text(text=songs, reply_markup=markup.as_markup())
    await state.set_state(PlaylistsStates.wait_choose)



@router.callback_query(F.data.in_({"sequential", "shuffle"}), PlaylistsStates.wait_choose)
async def change_song(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    order = callback_query.data

    # 1. Сохраняем исходный список в состоянии при первом вызове
    original_songs = data.get('original_list', playlists[data['name_playlist']])
    await state.update_data(original_list=original_songs)

    # 2. Работаем с копией исходного списка
    songs = original_songs.copy()

    if order == 'shuffle':
        import random
        # 3. Перемешиваем копию, не изменяя оригинал
        shuffled_songs = songs.copy()
        random.shuffle(shuffled_songs)
        await state.update_data(page=0, current_list=shuffled_songs)
    else:
        # 4. Для sequential используем оригинальную копию
        await state.update_data(page=0, current_list=songs)

    # 5. Получаем актуальные данные после обновления
    new_data = await state.get_data()
    song_list = new_data['current_list']
    page = new_data.get('page', 0)

    # 6. Логика отображения
    start = page * 1
    end = start + 1
    current_songs = song_list[start:end]

    markup = InlineKeyboardBuilder()

    # Кнопки навигации
    if page > 0:
        markup.add(types.InlineKeyboardButton(
            text="⬅️ Предыдущая",
            callback_data=f"previous:{page - 1}"
        ))
    if end < len(song_list):
        markup.add(types.InlineKeyboardButton(
            text="➡️ Следующая",
            callback_data=f"next:{page + 1}"
        ))
    markup.adjust(1, 1)

    songs_text = ("\n".join(current_songs) if current_songs else "Нет песен на этой странице.")

    await callback_query.message.edit_text(songs_text, reply_markup=markup.as_markup())
    await state.update_data(page=page)


@router.callback_query(F.data.startswith("previous:"), PlaylistsStates.wait_choose)
@router.callback_query(F.data.startswith("next:"), PlaylistsStates.wait_choose)
async def navigate_pages(callback_query: types.CallbackQuery, state: FSMContext):
    # 8. Обновляем только номер страницы
    data = await state.get_data()
    page = int(callback_query.data.split(":")[1])

    # 9. Проверка валидности номера страницы
    max_page = len(data['current_list']) - 1
    page = max(0, min(page, max_page))

    await state.update_data(page=page)

    # 10. Повторное отображение без изменения списка
    data = await state.get_data()
    song_list = data['current_list']

    # Логика отображения (как в change_song)
    start = page * 1
    end = start + 1
    current_songs = song_list[start:end]

    markup = InlineKeyboardBuilder()
    if page > 0:
        markup.add(types.InlineKeyboardButton(
            text="⬅️ Предыдущая",
            callback_data=f"previous:{page - 1}"
        ))
    if end < len(song_list):
        markup.add(types.InlineKeyboardButton(
            text="➡️ Следующая",
            callback_data=f"next:{page + 1}"
        ))
    markup.adjust(1, 1)

    # Сохраняем индикатор текущего режима
    songs_text = ("\n".join(current_songs) if current_songs else "Нет песен на этой странице.")

    await callback_query.message.edit_text(songs_text, reply_markup=markup.as_markup())

