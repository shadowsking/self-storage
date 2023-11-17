from django.core.management.base import BaseCommand
from service.handlers.handlers import bot
from telebot import custom_filters


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        bot.add_custom_filter(custom_filters.StateFilter(bot))
        bot.polling(skip_pending=True)
