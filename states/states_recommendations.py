from aiogram.fsm.state import State, StatesGroup

class RecommendationsStates(StatesGroup):
    choose_recommendations = State()
    wait_recommendations = State()