from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

from sources.postgres.sql_requests import (
    rename_playlist,
    delete_playlist,
    remove_song_from_playlist,
    create_playlist,
    get_all_playlists, rebase_song_from_playlist
)
from states.states_playlists import PlaylistsStates

router = Router()


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
            songs += f"\n{count}: {name}"
        await callback.message.edit_text(text=f"{songs}", reply_markup=markup.as_markup())
        await state.set_state(PlaylistsStates.choose_action)
    else:
        await callback.message.edit_text(text=f"Плейлист пуст")




#редактирование
@router.callback_query(F.data == "edit", PlaylistsStates.choose_action)
async def edit_menu(callback: types.CallbackQuery, state: FSMContext):
    markup = InlineKeyboardBuilder()
    data = await state.get_data()
    rename = types.InlineKeyboardButton(
        text="✏️ Изменить название",
        callback_data="rename"
    )
    edit_songs = types.InlineKeyboardButton(
        text="🎵 Редактировать песни",
        callback_data="edit_songs"
    )
    markup.add(rename, edit_songs)
    markup.adjust(1, 1)

    #Базовый плейлист нельзя удалить
    if data['name_playlist'] != 'Избранное':
        delete = types.InlineKeyboardButton(
            text="🗑️ Удалить плейлист",
            callback_data="delete"
        )
        markup.add(delete)

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
    user_id = callback.message.from_user.id

    data = await state.get_data()
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
    await callback.message.edit_text(text=f"Выберите действие над плейлистом {name_playlist}", markup = markup.as_markup())
    await state.set_state(PlaylistsStates.edit_songs)


#удаление песни
@router.callback_query(F.data == "delete_songs", PlaylistsStates.edit_songs)
async def delete_songs(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    data = await state.get_data()
    playlists = data['playlists']
    indexes = message.text.split(",")
    try:
        for i in indexes:
            if 0 <= int(i) < len(playlists[data['name_playlist']]):
                name_song = playlists[data['name_playlist']][int(i) - 1]
                ok = remove_song_from_playlist(data['name_playlist'], user_id, name_song)
                if not ok:
                    await message.answer("При удалении что-то пошло не так, попробуйте еще раз позже")
                else:
                    mes_text = f"Песня(и) удалена(ы)"
                    await message.answer(text=mes_text)

    except Exception as e:
        await message.answer(text=f"Ошибка:{e}")
        return

    await state.set_state(PlaylistsStates.action)



#функция перемещения песен между плейлистами
@router.callback_query(F.data == "rebase_song", PlaylistsStates.edit_songs)
async def rebase_song(callback: types.CallbackQuery, state: FSMContext):
    #TODO реализовать логику перемещения песен
    markup = InlineKeyboardBuilder()
    data = await state.get_data()
    playlists = data['playlists']
    mes_text = "Выберите в какой плейлист хотите переместить песню"
    for name in playlists.keys():
        markup.add(types.InlineKeyboardButton(text = str(name), callback_data= str(name)))
    markup.adjust(1, 1)
    await callback.message.edit_text(text=mes_text, reply_markup=markup.as_markup())
    await state.set_state(PlaylistsStates.rebase_song)


#функция перемещения песен между плейлистами
@router.callback_query(PlaylistsStates.rebase_song)
async def rebase_song(callback: types.CallbackQuery, state: FSMContext):
    new_playlist = callback.data
    await state.update_data(new_playlist=new_playlist)
    markup = InlineKeyboardBuilder()
    data = await state.get_data()
    data.update()
    playlists = data['playlists']
    old_playlists = data['name_playlists']
    mes_text = "Напишите название песни которую хотите переместить"
    count = 0
    for name in playlists[old_playlists]:
        count += 1
        mes_text += f"\n{count}: {name}"

    await callback.message.edit_text(text=mes_text, reply_markup=markup.as_markup())
    await state.set_state(PlaylistsStates.rebase_song)

@router.message(PlaylistsStates.rebase_song)
async def rebase_song(message: types.Message, state: FSMContext):
    data = await state.get_data()
    new_playlist = data['new_playlist']
    old_playlists = data['name_playlists']
    song_name = message.text
    ok = rebase_song_from_playlist(song_name, new_playlist, old_playlists)
    if not ok:
        await message.answer("При перемещение что-то пошло не так, попробуйте еще раз позже")
    else:
        mes_text = f"Песня перемещена в плейлист {new_playlist}"
        await message.answer(text=mes_text)


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
        songs += f"\n{song}"
    await callback.message.edit_text(text=songs, reply_markup=markup.as_markup())
    await state.set_state(PlaylistsStates.wait_choose)



@router.callback_query(F.data.in_({"sequential", "shuffle"}), PlaylistsStates.wait_choose)
async def change_song(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    playlists = data['playlists']
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
