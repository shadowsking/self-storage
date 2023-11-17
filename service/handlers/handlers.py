from telebot import TeleBot
from telebot.storage import StateMemoryStorage

from selfstorage.settings import TELEGRAM_TOKEN
from .states import States

state_storage = StateMemoryStorage()

bot = TeleBot(
    TELEGRAM_TOKEN,
    state_storage=state_storage
)


@bot.message_handler(commands=["start"])
def start_handler(message):
    # todo check user type and distribute the route
    bot.set_state(message.from_user.id, States.user_state, message.chat.id)
    bot.send_message(message.chat.id, text="Hello")


@bot.message_handler(state=States.admin_state)
def start_admin(message):
    bot.send_message(message.chat.id, text="Admin")


@bot.message_handler(state=States.user_state)
def start_user(message):
    bot.send_message(message.chat.id, text="User")
