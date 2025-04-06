from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import InputFile, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from pathlib import Path

from sqlalchemy.sql.functions import count

from sources.postgres.sql_requests import (
    rename_playlist,
    delete_playlist,
    remove_song_from_playlist,
    create_playlist,
    get_all_playlists, rebase_song_from_playlist
)
from states.states_playlists import PlaylistsStates

router = Router()

"""sample = {"Избранное": [
   {id: 1,
    "название": "Three little birds",
    "путь": "sources/audio/bob-marley-the-wailers-three-little-birds.mp3"
    },
    {   id: 2,
    "название": "Ямайка",
    "путь": "sources/audio/Comedoz - Ямайка.mp3"
    }
]
}"""

#стартовое окно
@router.message(F.text.endswith("Мои плейлисты"))
async def start_recommendations(message: types.Message, state: FSMContext):
    # запрос в БД

    user_id = message.from_user.id
    playlists = get_all_playlists(user_id)


    await state.update_data(playlists=playlists)

    markup = InlineKeyboardBuilder()
    create = types.InlineKeyboardButton(
        text="➕ Создать плейлист",
        callback_data="create"
    )
    markup.add(create)
    for name in playlists.keys():
        markup.add(types.InlineKeyboardButton(text = str(name), callback_data= str(name)))
    markup.adjust(1, 1)


    sent_message = await message.answer(text="Ваши плейлисты:", reply_markup=markup.as_markup())
    await state.update_data(last_message_id=sent_message.message_id)
    await state.set_state(PlaylistsStates.choose_playlist)


#создание плейлиста
@router.callback_query(F.data == "create", PlaylistsStates.choose_playlist)
async def create(callback: types.CallbackQuery, state: FSMContext):
    mes_text = "Напишите название плейлиста"
    await callback.message.edit_text(text=mes_text)

    await state.set_state(PlaylistsStates.create_playlist)


@router.message(F.text, PlaylistsStates.create_playlist)
async def create(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    text = message.text
    data = await state.get_data()
    playlists = data['playlists']
    if text not in playlists:
        ok = create_playlist(user_id, text)
        if not ok:
            await message.answer("Что-то пошло не так. Попробуйте еще раз позже")
        else:
            mes_text = f"Плейлист {message.text} создан"
            await message.answer(text=mes_text)
    else:
        await message.answer(text="Такой плейлист уже существует")
        return
    await state.set_state(PlaylistsStates.action)


@router.callback_query(PlaylistsStates.choose_playlist)
async def playlist_menu(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'create':
        return

    name_playlist = callback.data
    await state.update_data(name_playlist=name_playlist)
    data = await state.get_data()
    playlists = data['playlists']

    markup = InlineKeyboardBuilder()
    listen = types.InlineKeyboardButton(
        text="🎧 Прослушать плейлист",
        callback_data="listen"
    )
    edit = types.InlineKeyboardButton(
        text="✏️ Редактировать плейлист",
        callback_data="edit"
    )
    markup.add(listen, edit,)
    markup.adjust(1, 1)

    songs = ""
    count = 0
    if len(playlists[name_playlist]) != 0:
        for name in playlists[name_playlist]:
            count += 1
            songs += f"\n{count}: {name['название']}"
        await callback.message.edit_text(text=f"{songs}", reply_markup=markup.as_markup())
        await state.set_state(PlaylistsStates.choose_action)
    else:
        await callback.message.edit_text(text=f"Плейлист пуст")


#редактирование
@router.callback_query(F.data == "edit", PlaylistsStates.choose_action)
async def edit_menu(callback: types.CallbackQuery, state: FSMContext):
    markup = InlineKeyboardBuilder()
    data = await state.get_data()
    edit_songs = types.InlineKeyboardButton(
        text="🎵 Редактировать песни",
        callback_data="edit_songs"
    )
    markup.add( edit_songs)

    #Базовый плейлист нельзя удалить
    if data['name_playlist'] != 'Избранное':
        delete = types.InlineKeyboardButton(
            text="🗑️ Удалить плейлист",
            callback_data="delete"
        )
        rename = types.InlineKeyboardButton(
            text="✏️ Изменить название",
            callback_data="rename"
        )
        markup.add(delete, rename)
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
    user_id = message.from_user.id

    data = await state.get_data()
    try:
        ok = rename_playlist(data['name_playlist'], message.text, user_id)
        if not ok:
            await message.answer("Что-то пошло не так. Попробуйте еще раз позже")
        else:
            mes_text = f"Плейлист переименован на {message.text}"
            await message.answer(text=mes_text)
    except KeyError:
        await message.answer(text="Такого плейлиста нет")

    await state.set_state(PlaylistsStates.action)


#удаление плейлиста
@router.callback_query(F.data == "delete", PlaylistsStates.wait_choose)
async def delete(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    data = await state.get_data()
    name_playlist = data['name_playlist']
    mes_text = f"Плейлист {data['name_playlist']} удален"
    try:
        ok = delete_playlist(data['name_playlist'], user_id)
        if not ok:
            await callback.message.answer("Что-то пошло не так. Попробуйте еще раз позже")
        else:
            await callback.message.edit_text(text=mes_text)
    except KeyError:
        await callback.message.edit_text(text="Такого плейлиста нет")

    await state.set_state(PlaylistsStates.action)


#редактрование песен
@router.callback_query(F.data == "edit_songs", PlaylistsStates.wait_choose)
async def edit_songs(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    name_playlist = data['name_playlist']
    markup = InlineKeyboardBuilder()
    delete_songs = types.InlineKeyboardButton(
        text="🗑️ Удалить песни",
        callback_data="delete_songs"
    )
    rebase_song = types.InlineKeyboardButton(
        text="🎵 Переместить песни",
        callback_data="rebase_song"
    )
    markup.add(delete_songs, rebase_song)
    markup.adjust(1, 1)
    await callback.message.edit_text(text=f"Выберите действие над плейлистом {name_playlist}", reply_markup = markup.as_markup())
    await state.set_state(PlaylistsStates.edit_songs)


#удаление песни
@router.callback_query(F.data == "delete_songs", PlaylistsStates.edit_songs)
async def rename(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    playlists = data['playlists']
    name_playlist = data['name_playlist']
    count = 0
    mes_text = "Напишите индекс песни для удаления"
    for name in playlists[name_playlist]:
        count += 1
        mes_text += f"\n{count}: {name['название']}"

    await callback.message.edit_text(text=mes_text)
    await state.set_state(PlaylistsStates.edit_songs)


@router.message(F.text, PlaylistsStates.edit_songs)
async def delete_songs(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    data = await state.get_data()
    name_playlist = data['name_playlist']
    playlists = data['playlists']
    ind = message.text
    try:
        if 0 <= int(ind) - 1 < len(playlists[name_playlist]):
            name_song = playlists[name_playlist][int(ind) - 1]['название']
            ok = remove_song_from_playlist(data['name_playlist'], user_id, name_song)
            if not ok:
                await message.answer("При удалении что-то пошло не так, попробуйте еще раз позже")
            else:
                mes_text = f"Песня удалена"
                await message.answer(text=mes_text)

    except Exception as e:
        await message.answer(text=f"Ошибка:{e}")
        return

    await state.set_state(PlaylistsStates.action)



#функция перемещения песен между плейлистами
@router.callback_query(F.data == "rebase_song", PlaylistsStates.edit_songs)
async def rebase_song(callback: types.CallbackQuery, state: FSMContext):
    markup = InlineKeyboardBuilder()
    data = await state.get_data()
    playlists = data['playlists']
    name_playlist = data['name_playlist']
    mes_text = "Выберите в какой плейлист хотите переместить песню"
    for name in playlists.keys():
        if name != name_playlist:
            markup.add(types.InlineKeyboardButton(text = str(name), callback_data= str(name)))
    markup.adjust(1, 1)
    await callback.message.edit_text(text=mes_text, reply_markup=markup.as_markup())
    await state.set_state(PlaylistsStates.rebase_song)


@router.callback_query(PlaylistsStates.rebase_song)
async def rebase_song(callback: types.CallbackQuery, state: FSMContext):
    new_playlist = callback.data
    await state.update_data(new_playlist=new_playlist)
    data = await state.get_data()
    data.update()
    playlists = data['playlists']
    old_playlists = data['name_playlist']
    mes_text = "Напишите название песни которую хотите переместить"
    count = 0
    for name in playlists[old_playlists]:
        count += 1
        mes_text += f"\n{count}: {name['название']}"

    await callback.message.edit_text(text=mes_text)
    await state.set_state(PlaylistsStates.rebase_song)

@router.message(PlaylistsStates.rebase_song)
async def rebase_song(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        new_playlist = data['new_playlist']
        old_playlists = data['name_playlist']
        song_name = message.text
        ok = rebase_song_from_playlist(song_name, new_playlist, old_playlists)
        if not ok:
            await message.answer("При перемещение что-то пошло не так, попробуйте еще раз позже")
        else:
            mes_text = f"Песня перемещена в плейлист {new_playlist}"
            await message.answer(text=mes_text)
    except KeyError as e:
        await message.answer(text="Такой песни нет")


#прослушивание песен
@router.callback_query(F.data == "listen", PlaylistsStates.choose_action)
async def listen_menu(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    playlists = data['playlists']
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
        songs += f"\n{song['название']}"
    await callback.message.edit_text(text=songs, reply_markup=markup.as_markup())
    await state.set_state(PlaylistsStates.wait_choose)


async def send_audio_message(message: types.Message, track: dict, markup: InlineKeyboardBuilder):
    """Унифицированная отправка аудио с обработкой ошибок"""
    try:
        file_path = Path(track['путь'])
        if not file_path.exists():
            raise FileNotFoundError(f"Файл {track['путь']} не найден")

        return await message.answer_audio(
            audio=FSInputFile(file_path),
            title=track.get('название', 'Без названия'),
            performer=track.get('исполнитель', 'Неизвестен'),
            reply_markup=markup.as_markup()
        )
    except Exception as e:
        error_message = f"❌ Ошибка: {str(e)}"
        await message.answer(error_message)
        return None


@router.callback_query(F.data.in_({"sequential", "shuffle"}), PlaylistsStates.wait_choose)
async def change_song(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    playlists = data['playlists']
    order = callback.data

    original_tracks = data.get('original_list', playlists[data['name_playlist']].copy())
    tracks = original_tracks.copy()

    if order == 'shuffle':
        import random
        random.shuffle(tracks)

    await state.update_data(
        page=0,
        current_list=tracks,
        original_list=original_tracks,
        items_per_page=10  # Добавляем параметр элементов на страницу
    )

    new_data = await state.get_data()
    track_list = new_data['current_list']
    page = new_data.get('page', 0)
    per_page = new_data['items_per_page']

    markup = InlineKeyboardBuilder()

    # Рассчитываем диапазон треков
    start = page * per_page
    end = start + per_page
    current_page_tracks = track_list[start:end]

    # Добавляем кнопки для каждого трека на странице
    for idx, track in enumerate(current_page_tracks, start=1):
        markup.button(
            text=f"{idx}. {track['название'][:15]}",
            callback_data=f"track_{start + idx - 1}"
        )

    # Добавляем кнопки пагинации
    if page > 0:
        markup.button(text="⬅️ Предыдущая", callback_data=f"prev_page_{page - 1}")
    if end < len(track_list):
        markup.button(text="➡️ Следующая", callback_data=f"next_page_{page + 1}")

    markup.adjust(2, repeat=True)

    try:
        await callback.message.delete()
        await callback.message.answer(
            f"🎧 Страница {page + 1}\nВыберите трек:",
            reply_markup=markup.as_markup()
        )
    except Exception as e:
        await callback.message.answer(f"⚠️ Ошибка: {str(e)}")


@router.callback_query(F.data.startswith("track_"), PlaylistsStates.wait_choose)
async def play_selected_track(callback: types.CallbackQuery, state: FSMContext):
    track_index = int(callback.data.split("_")[1])
    data = await state.get_data()
    track_list = data['current_list']

    markup = InlineKeyboardBuilder()
    try:
        current_track = track_list[track_index]
        await send_audio_message(callback.message, current_track, markup)
    except IndexError:
        await callback.message.answer("🚫 Трек не найден")


@router.callback_query(F.data.startswith("prev_page_"), PlaylistsStates.wait_choose)
@router.callback_query(F.data.startswith("next_page_"), PlaylistsStates.wait_choose)
async def navigate_pages(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    track_list = data['current_list']
    per_page = data['items_per_page']
    action = callback.data.split("_")[:2]
    page = callback.data.split("_")[2]
    print(callback.data)
    print(action, page)
    new_page = int(page)

    await state.update_data(page=new_page)

    markup = InlineKeyboardBuilder()
    start = new_page * per_page
    end = start + per_page
    current_page_tracks = track_list[start:end]

    for idx, track in enumerate(current_page_tracks, start=1):
        markup.button(
            text=f"{idx}. {track['название'][:15]}",
            callback_data=f"track_{start + idx - 1}"
        )

    if new_page > 0:
        markup.button(text="⬅️ Предыдущая", callback_data=f"prev_page_{new_page - 1}")
    if end < len(track_list):
        markup.button(text="➡️ Следующая", callback_data=f"next_page_{new_page + 1}")

    markup.adjust(2, repeat=True)

    try:
        await callback.message.edit_text(
            f"🎧 Страница {new_page + 1}\nВыберите трек:",
            reply_markup=markup.as_markup()
        )
    except Exception as e:
        await callback.message.answer(f"⚠️ Ошибка при обновлении: {str(e)}")
