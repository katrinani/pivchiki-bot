from aiogram import F, types, Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

from states.states_recommendations import RecommendationsStates

router = Router()
#TODO убрать дудос сообщений

#клавиатура для оценок
grade_markup =InlineKeyboardBuilder()
like = types.InlineKeyboardButton(
    text="❤️ Понравилось",
    callback_data="like"
)
dislike = types.InlineKeyboardButton(
    text="👎 Не понравилось",
    callback_data="dislike"
)
playlist = types.InlineKeyboardButton(
    text="➕ Добавить в плейлист",
    callback_data="add_in_playlist"
)

grade_markup.add(like, dislike, playlist)
grade_markup.adjust(1, 1)


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
async def user_rec(callback: types.CallbackQuery, state: FSMContext):
    mes_text = ("Вот плейлист пользователя с таким же вкусом:"
                "\nSong\nSong\nSong\nSong\nSong\nSong\nSong")
    await callback.message.edit_text(text=mes_text)
    await state.set_state(RecommendationsStates.wait_recommendations)

# Похожие на ваш выбор
@router.callback_query(F.data == "similar", RecommendationsStates.choose_recommendations)
async def similar_rec(callback: types.CallbackQuery, state: FSMContext):
    mes_text = ("Вот плейлист похожий на ваш:"
                "\nSong\nSong\nSong\nSong\nSong\nSong\nSong")
    await callback.message.edit_text(text=mes_text)
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


#sad mood
@router.callback_query(F.data == "sad", RecommendationsStates.choose_recommendations)
async def sad_mood(callback: types.CallbackQuery, state: FSMContext):
    mes_text = "Вот грустный плейлист:\n"
    songs = ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5", "Song 6", "Song 7", "Song 8", "Song 9", "Song 10"]

    for song in songs:
        mes_text += f"{song}\n"
        await callback.message.answer(text=mes_text, reply_markup=grade_markup.as_markup())

    await state.set_state(RecommendationsStates.wait_recommendations)

#happy mood
@router.callback_query(F.data == "happy", RecommendationsStates.choose_recommendations)
async def happy_mood(callback: types.CallbackQuery, state: FSMContext):
    mes_text = "Вот весёлый плейлист:\n"
    songs = ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5", "Song 6", "Song 7", "Song 8", "Song 9", "Song 10"]

    for song in songs:
        mes_text += f"{song}\n"
        await callback.message.answer(text=mes_text, reply_markup=grade_markup.as_markup())

    await state.set_state(RecommendationsStates.wait_recommendations)

#relax mood
@router.callback_query(F.data == "relax", RecommendationsStates.choose_recommendations)
async def relax_mood(callback: types.CallbackQuery, state: FSMContext):
    mes_text = "Вот спокойный плейлист:\n"
    songs = ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5", "Song 6", "Song 7", "Song 8", "Song 9", "Song 10"]

    for song in songs:
        mes_text += f"{song}\n"
        await callback.message.answer(text=mes_text,  reply_markup=grade_markup.as_markup())

    await state.set_state(RecommendationsStates.wait_recommendations)

#cheerful mood
@router.callback_query(F.data == "cheerful", RecommendationsStates.choose_recommendations)
async def cheerful_mood(callback: types.CallbackQuery, state: FSMContext):
    mes_text = "Вот бодрый плейлист:\n"
    songs = ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5", "Song 6", "Song 7", "Song 8", "Song 9", "Song 10"]

    for song in songs:
        mes_text += f"{song}\n"
        await callback.message.answer(text=mes_text, reply_markup=grade_markup.as_markup())

    await state.set_state(RecommendationsStates.wait_recommendations)