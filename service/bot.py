from environs import Env
from telegram.ext import Updater, CommandHandler

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


env = Env()
env.read_env()


def greet_user(update, context):
    update.message.reply_text('Привет! Это бот для управления складом')


def main():
    tg_token = env.str('TG_BOT_TOKEN')

    mybot = Updater(token=tg_token, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
