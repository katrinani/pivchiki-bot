"""
2. Поиск музыки
Пользователь нажимает кнопку 🎵 Поиск музыки.
Бот предлагает выбрать тип поиска:
🔍 По названию
✍️ По автору
🎤 По голосовому сообщению
Пользователь выбирает тип поиска:
Если выбран 🔍 По названию или ✍️ По автору, бот запрашивает текстовый ввод.
Если выбран 🎤 По голосовому сообщению, бот запрашивает голосовое сообщение.
Бот обрабатывает запрос и выдает список до 10 песен в формате:
Copy
1. Название песни - Автор
2. Название песни - Автор
...
Под списком кнопки:
Выбрать песню (1-10) (кнопки с номерами)
🔄 Повторить поиск
Если пользователь выбирает песню:
Бот отправляет песню в формате .mp3.
Под песней кнопки:
➕ Добавить в плейлист
🔙 Назад к списку
Если пользователь нажимает ➕ Добавить в плейлист, бот предлагает выбрать плейлист из списка (см. раздел "Мои плейлисты").
"""
from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

# импортируем статусы
from states.states_search import SearchStates

# парсер из ютуба
from sources.parsers.parser_youtube import find_song, download_song

router = Router()

@router.callback_query(F.data == 'search')
async def start_search(callback: types.CallbackQuery, state: FSMContext):
    # TODO сохранить и использовать для удаления callback.message.message_id

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
    await callback.message.answer(text="Выберите тип поиска:", reply_markup=markup.as_markup())
    await state.set_state(SearchStates.choose_method)


@router.callback_query(F.data == "text", SearchStates.choose_method)
async def get_info_about_song(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Принято! Тогда введите свой запрос. Укажите имя и/или автора:")
    await state.set_state(SearchStates.wait_info_about_song)


@router.message(F.text, SearchStates.wait_info_about_song)
async def request_processing(message: types.Message, state: FSMContext):
    await message.answer("Ищу! Минутку...")
    # result_search, data, count = find_song(message.text)
    result_search = """
Найденные варианты:
1. The neighborhood playlist - Melodylian
2. The Neighbourhood - Sweater Weather (Official Video) - The Neighbourhood
3. The Neighbourhood - Softcore (Official Audio) - The Neighbourhood
4. The Neighbourhood - Reflections (Official Audio) - The Neighbourhood
5. The Neighbourhood - W.D.Y.W.F.M? (Official Audio) - The Neighbourhood
6. The Neighbourhood - You Get Me So High (Official Audio) - The Neighbourhood
7. The Neighbourhood - Afraid (Official Audio) - The Neighbourhood
8. The Neighbourhood - A Little Death (Official Audio) - The Neighbourhood
9. the neighbourhood - r.i.p. 2 my youth // slowed + reverb - kouyou
10. The Neighbourhood - Reflections (Lyrics) - Aura Melodies

Введите номер трека для скачивания или повторите поиск:
    """
    count = 10

    # TODO проверка что хоть что-то нашлось
    # сохраняем данные поиска
    # await state.update_data({"result": data})

    markup = InlineKeyboardBuilder()
    for i in range(count):
        btn = types.InlineKeyboardButton(
            text=f"{i + 1}",
            callback_data=f"song_{i + 1}"
        )
        markup.add(btn)

    second_time = types.InlineKeyboardButton(
        text="🔄 Повторить поиск",
        callback_data="search"
    )
    markup.add(second_time)
    markup.adjust(5, 5, 1)

    await message.answer(text=result_search, reply_markup=markup.as_markup())
    await state.set_state(SearchStates.send_song)


@router.callback_query(
    F.data.in_([f"song_{i + 1}" for i in range(10)]),
    SearchStates.send_song
)
async def send_song(callback: types.CallbackQuery, state: FSMContext):
    # получаем результаты хендлера выше
    # data = await state.get_data()
    # result = data["result"]

    path = "sources/songs"

    markup = InlineKeyboardBuilder()
    markup.add(types.InlineKeyboardButton(
        text="➕ Добавить в плейлист",
        callback_data="add_song"
    ))

    # path_with_song = download_song(int(callback.data), result, path)
    path_with_song = path + "/The neighborhood playlist.mp3"
    # TODO проверки что скачалось
    file = FSInputFile(path_with_song)
    await callback.message.answer_audio(file, reply_markup=markup.as_markup())
    await state.clear()
