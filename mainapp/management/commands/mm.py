from django.core.management import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):

    help = ("This command is used for call makemessages and"
            "uses flags, --locale, --ignore and --no-location")

    def handle(self, *args, **kwargs):
        call_command('makemessages', '--locale=ru', '--ignore=venv', '--no-location')
