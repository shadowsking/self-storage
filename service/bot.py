from environs import Env
from telegram.ext import Updater, CommandHandler

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


env = Env()
env.read_env()


def greet_user(update, context):
    message = update.message
    print(message)

    welcome_message = (
        f'Привет, {update.message.from_user.first_name}!\n'
        '\n'
        'Я бот SelfStorage. Храните свои вещи без забот на наших складах.\n'
        '\n'
        '- Хранение сезонных, крупных вещей:лыжи, сноуборды, велосипеды. \n'
        '- Хранение вещей на время переезда. \n'
        '- Освобождение дома от крупных, но дорогих вещей, которые хочется сохранить.'
    )
    image_path = 'static/hello.png'
    with open(image_path, 'rb') as photo:
        update.message.reply_photo(photo, caption=welcome_message)


def main():
    tg_token = env.str('TG_BOT_TOKEN')

    updater = Updater(token=tg_token, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))

    logging.info("Бот стартовал")
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
