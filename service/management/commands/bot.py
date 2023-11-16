from django.core.management.base import BaseCommand

from service.bot import main


class Command(BaseCommand):
    def handle(self, *args, **options):
        main()