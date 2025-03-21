from aiogram.fsm.state import State, StatesGroup


class SearchStates(StatesGroup):
    choose_method = State()
    wait_info_about_song = State()
    send_song = State()