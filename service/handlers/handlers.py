from telebot import TeleBot
from telebot import types
from telebot.storage import StateMemoryStorage

from selfstorage.settings import TELEGRAM_TOKEN
# from .states import States

state_storage = StateMemoryStorage()

bot = TeleBot(
    TELEGRAM_TOKEN,
)


@bot.message_handler(commands=["start"])
def start_handler(message):
    try:
        welcome_message = (
            f'Привет, {message.from_user.first_name}!\n'
            '\n'
            'Я бот SelfStorage. Храните свои вещи без забот на наших складах.\n'
            '\n'
            '- Хранение сезонных, крупных вещей: лыжи, сноуборды, велосипеды. \n'
            '- Хранение вещей на время переезда. \n'
            '- Освобождение дома от крупных, но дорогих вещей, которые хочется сохранить.'
        )

        markup = types.InlineKeyboardMarkup()
        btn_rules = types.InlineKeyboardButton(
            text="Правила",
            callback_data="rules"
            )
        btn_order = types.InlineKeyboardButton(
            text="Заказ бокса",
            callback_data="order"
            )
        btn_storage = types.InlineKeyboardButton(
            text="Ваше хранение",
            callback_data="storage"
            )

        markup.add(btn_rules, btn_order, btn_storage)

        image_path = 'static/hello.png'

        with open(image_path, 'rb') as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption=welcome_message,
                reply_markup=markup
                )
    except Exception as e:
        print(f"Error: {e}")
