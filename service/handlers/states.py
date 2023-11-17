from telebot.handler_backends import State, StatesGroup


class States(StatesGroup):
    user_state = State()
    admin_state = State()
