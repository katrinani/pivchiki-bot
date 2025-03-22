from aiogram import F, types, Router, Bot
from aiogram.fsm.context import FSMContext
import os

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
    await bot.download(message.audio.file_id, destination=file_path)
    # TODO поиск песни по алгоритму
    # TODO сохранение песни и метрик в бд
    mes_text = f"Песня {message.audio.file_name} успешно загружена в плейлист 'Избранное'"
    await message.answer(text=mes_text)
    await state.clear()


@router.message(DownloadStates.wait_mp3)
async def dont_load_song(message: types.Message, state: FSMContext):
    mes_text = "К сожалению это не песня в формате .mp3\nПопробуйте отправить снова"
    await message.edit_message_text(text=mes_text)
    await state.set_state(DownloadStates.wait_mp3)
