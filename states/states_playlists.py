from aiogram.fsm.state import State, StatesGroup

class PlaylistsStates(StatesGroup):
    choose_playlist = State()
    choose_action = State()
    wait_choose = State()
    rename = State()
    edit_songs = State()
    create_playlist = State()
    rebase_song= State()
    action = State()