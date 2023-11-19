from telebot import TeleBot
from telebot import types
from telebot.storage import StateMemoryStorage

from selfstorage.settings import TELEGRAM_TOKEN
from users.models import User
from .states import States

state_storage = StateMemoryStorage()

bot = TeleBot(
    TELEGRAM_TOKEN,
    # state_storage=state_storage
)


@bot.message_handler(commands=["start"])
def client_greeting(message):
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


@bot.callback_query_handler(func=lambda call: call.data == "rules")
def rules_handler(call):

    rules_text = (
        "Правила хранения:\n"
        "1. Запрещено хранить легко воспламеняющиеся или взрывоопасные вещества.\n"
        "2. Запрещено хранить продукты питания или другие скверносъедобные предметы.\n"
        "3. Запрещено хранить животных и насекомых.\n"
        "4. Запрещено хранить запрещенные к обороту вещи согласно законодательству.\n"
        "5. Нельзя хранить вещи, которые создают неприятный запах.\n"
        "\n"
        "Выберите действие:"
    )

    markup = types.InlineKeyboardMarkup()
    btn_return = types.InlineKeyboardButton(
        text="Вернуться в меню",
        callback_data="return_to_menu"
    )
    btn_allowed_items = types.InlineKeyboardButton(
        text="Разрешенные предметы",
        callback_data="allowed_items"
    )

    markup.add(btn_return, btn_allowed_items)

    bot.send_message(call.message.chat.id, rules_text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "allowed_items")
def allowed_items_handler(call):

    allowed_items_text = (
        "Разрешенные предметы для хранения:\n"
        "- Сезонные спортивные товары (лыжи, сноуборды, велосипеды).\n"
        "- Домашние вещи и мебель, которые не нарушают правила безопасности.\n"
        "- Личные вещи и предметы быта.\n"
        "- Специальное оборудование для хобби и развлечений.\n"
        "\n"
        "Выберите действие:"
    )

    markup = types.InlineKeyboardMarkup()
    btn_return = types.InlineKeyboardButton(
        text="Вернуться в меню",
        callback_data="return_to_menu"
    )

    markup.add(btn_return)

    bot.send_message(call.message.chat.id, allowed_items_text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "return_to_menu")
def return_to_menu_handler(call):
    text = "Выберите опцию"

    markup = types.InlineKeyboardMarkup()
    btn_rules = types.InlineKeyboardButton(
        text="Правила",
        callback_data="rules"
    )
    btn_order = types.InlineKeyboardButton(
        text="Заказ Бокса",
        callback_data="order"
    )
    btn_storage = types.InlineKeyboardButton(
        text="Ваше хранение",
        callback_data="storage"
    )

    markup.add(btn_rules, btn_order, btn_storage)

    bot.send_message(call.message.chat.id, text, reply_markup=markup)


    @bot.callback_query_handler(func=lambda call: call.data == "order")
    def order_button_handler(call):
        user_id = call.from_user.id
        bot.send_message(call.message.chat.id, "Введите ваше имя:")
        bot.register_next_step_handler(call.message, get_user_name, user_id=user_id)


