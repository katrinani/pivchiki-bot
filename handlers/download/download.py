from aiogram import F, types, Router, Bot
from aiogram.fsm.context import FSMContext
import os

from sources.postgres.sql_requests import save_mp3, rebase_song_from_playlist
from sources.search.search import extract_features
from states.states_download import DownloadStates

router = Router()

@router.message(F.text.endswith("Загрузить трек"))
async def start_load(message: types.Message, state: FSMContext):

    mes_text = "Хорошо! Отправьте пожалуйста вашу песню в формате .mp3"
    await message.answer(text=mes_text)
    await state.set_state(DownloadStates.wait_mp3)


@router.message(F.audio, DownloadStates.wait_mp3)
async def load_song(message: types.Message, state: FSMContext, bot: Bot):
    sent_message = await message.answer("Обрабатываю, минутку...")
    await state.update_data(search_message_id=sent_message.message_id)

    if not os.path.exists('sources/songs'):
        os.makedirs('sources/songs')

    file_path = f"sources/songs/{message.audio.file_name}"
    # Проверяем существование файла
    if os.path.exists(file_path):
        print(f"Файл {file_path} уже существует!")
        mes_text = f"Песня {message.audio.file_name} успешно загружена"
        await message.answer(text=mes_text)
        await state.clear()
        return
    else:
        # Файла нет, можно скачивать
        await bot.download(message.audio.file_id, destination=file_path)

    # создаем вектор VGGish
    features: list[float] = extract_features(file_path).tolist()

    # сохранение в бд
    song_id, ok = await save_mp3(
        file_path,
        message.audio.file_name,
        features
    )
    if not ok:
        await message.answer("Не удалось сохранить песню. Попробуйте позже еще раз")
    else:
        ok = rebase_song_from_playlist(message.from_user.id ,message.audio.file_name, "Избранное")
        if not ok:
            await message.answer("Не удалось сохранить песню. Попробуйте позже еще раз")
        else:
            mes_text = f"Песня {message.audio.file_name} успешно загружена в плейлист 'Избранное'"
            await message.answer(text=mes_text)

    await state.clear()


@router.message(DownloadStates.wait_mp3)
async def dont_load_song(message: types.Message, state: FSMContext):
    mes_text = "К сожалению это не песня в формате .mp3\nПопробуйте отправить снова"
    await message.edit_message_text(text=mes_text)
    await state.set_state(DownloadStates.wait_mp3)
