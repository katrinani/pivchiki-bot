import os
from os import remove
from aiogram import F, types, Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

from sources.search.search import find_most_similar_song, extract_features, to_svd
# импортируем статусы
from states.states_search import SearchStates
# парсер из ютуба
from sources.parsers.YouTubeBomber import find_in_youtube, download_song
# методы бд
from sources.postgres.sql_requests import save_search_history, save_mp3, rebase_song_from_playlist

router = Router()


@router.message(F.text.endswith("Поиск музыки"))
async def start_search(message: types.Message, state: FSMContext):
    await state.clear()

    markup = InlineKeyboardBuilder()
    by_text = types.InlineKeyboardButton(
        text="✍️ По текстовому вводу",
        callback_data="text"
    )
    by_audio = types.InlineKeyboardButton(
        text="🎤 По голосовому сообщению",
        callback_data="audio"
    )
    markup.add(by_text, by_audio)
    markup.adjust(1, 1)

    sent_message = await message.answer(text="Выберите тип поиска:", reply_markup=markup.as_markup())
    await state.update_data(last_message_id=sent_message.message_id)
    await state.set_state(SearchStates.choose_method)


# случай, если текст
@router.callback_query(F.data == "text", SearchStates.choose_method)
async def get_info_about_song(callback: types.CallbackQuery, state: FSMContext):
    mes_text = "Принято! Тогда введите свой запрос. Укажите название песни и/или автора:"

    markup = InlineKeyboardBuilder()
    cansel = types.InlineKeyboardButton(
        text="Отменить поиск",
        callback_data="cansel"
    )
    markup.add(cansel)

    await callback.message.edit_text(text=mes_text, reply_markup=markup.as_markup())
    await state.set_state(SearchStates.wait_info_about_song)


@router.message(F.text, SearchStates.wait_info_about_song)
async def request_processing(message: types.Message, state: FSMContext):
    # сохранить в бд запрос и время запроса
    user_id = message.from_user.id
    save_search_history(user_id, message.text)

    sent_message = await message.answer("Ищу! Минутку...")
    await state.update_data(search_message_id=sent_message.message_id)

    answer = find_in_youtube(message.text)
    if not answer[0]:
        await message.answer(answer[1])
        return

    result = answer[1]
    data = answer[2]
    count = answer[3]

    # сохраняем данные поиска
    await state.update_data({"result": data})

    markup = InlineKeyboardBuilder()
    for i in range(count):
        btn = types.InlineKeyboardButton(
            text=f"{i + 1}",
            callback_data=f"song_{i + 1}"
        )
        markup.add(btn)
    cansel = types.InlineKeyboardButton(
        text="Отменить поиск",
        callback_data="cansel"
    )
    markup.add(cansel)

    markup.adjust(5, 5, 1)

    data = await state.get_data()
    await message.bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=data["search_message_id"],
        text=result,
        reply_markup=markup.as_markup()
    )
    await state.set_state(SearchStates.send_song)


@router.callback_query(F.data == "cansel")
async def cansel_search(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Отменяю поиск")
    await state.clear()


@router.callback_query(
    F.data.in_([f"song_{i + 1}" for i in range(10)]),
    SearchStates.send_song
)
async def send_song(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Замечательный выбор! Загружаю...")
    data = await state.get_data()
    result = data["result"]

    path = "sources/songs"
    name = result[int(callback.data[-1]) - 1]

    callback_data = f"add_song:{name}"

    # Проверяем длину callback_data
    if len(callback_data.encode('utf-8')) > 64:
        callback_data = callback_data[:64]  # Обрезаем до 64 байт

    markup = InlineKeyboardBuilder()
    markup.add(types.InlineKeyboardButton(
        text="➕ Добавить в Избранное",
        callback_data=callback_data  # Используем безопасную версию
    ))

    file_path = os.path.join(path, f"{name}.mp3")  # или другой формат

    # Проверяем существование файла
    if os.path.exists(file_path):
        print(f"Трек {name} уже существует, пропускаем загрузку")
    else:
        success, track_data = download_song(result, int(callback.data[-1]), path)

        print(success, track_data)

        if not success:
            await callback.message.answer("Не удалось скачать, попробуйте позже еще раз")
            return

    file = FSInputFile(file_path)
    await callback.message.answer_audio(file, reply_markup=markup.as_markup())
    await state.clear()


# случай, если гс
@router.callback_query(F.data == "audio", SearchStates.choose_method)
async def get_voice(callback: types.CallbackQuery, state: FSMContext):
    mes_text = "Хорошо! Тогда запишите голосовое сообщение, где будет слышно песню, примерно на 30 сек."

    markup = InlineKeyboardBuilder()
    cansel = types.InlineKeyboardButton(
        text="Отменить поиск",
        callback_data="cansel"
    )
    markup.add(cansel)

    await callback.message.edit_text(text=mes_text, reply_markup=markup.as_markup())
    await state.set_state(SearchStates.wait_audio)


@router.message(F.voice, SearchStates.wait_audio)
async def voice_processing(message: types.Message, state: FSMContext, bot: Bot):
    await message.answer("Услышал вас. Уже ищу!")
    file_path = f"{message.voice.file_id}.ogg"
    await bot.download(message.voice.file_id, destination=file_path)

    nearest_song, best_name, max_similarity = find_most_similar_song(file_path)

    if nearest_song == "":
        text = "К сожалению я не смог найти песню. Попробуйте повторить поиск"
        await message.answer(text=text)
        await state.clear()

    # сохранить в бд запрос и время запроса
    user_id = message.from_user.id
    save_search_history(user_id, best_name)

    markup = InlineKeyboardBuilder()
    markup.add(types.InlineKeyboardButton(
        text="➕ Добавить в Избранное",
        callback_data=f"add_song:{best_name}"
    ))

    file = FSInputFile(nearest_song)
    mes_text = f"Я нашел:\n{best_name}"
    await message.answer_audio(file, caption=mes_text, reply_markup=markup.as_markup())
    remove(file_path)
    # сохраняем имя песни
    await state.update_data({"song_name": file.filename})
    await state.clear()



@router.message(SearchStates.wait_audio)
async def voice_processing(message: types.Message, state: FSMContext):
    mes_text = "К сожалению это не голосовое сообщение\nПопробуйте записать его снова"
    await message.answer(text=mes_text)
    await state.set_state(SearchStates.wait_audio)


@router.callback_query(F.data.startswith("add_song:"))
async def add_new_song(callback: types.CallbackQuery, state: FSMContext):
    song_name = callback.data.split(":")[1]

    ok = rebase_song_from_playlist(song_name, "Избранное")
    if not ok:
        await callback.message.answer("Не удалось сохранить песню. Попробуйте позже еще раз")
    else:
        mes_text = f"Песня {song_name} успешно загружена в плейлист 'Избранное'"
        await callback.message.answer(text=mes_text)