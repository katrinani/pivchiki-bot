from aiogram.fsm.state import State, StatesGroup

class DownloadStates(StatesGroup):
    wait_mp3 = State()