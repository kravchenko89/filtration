from django.core.management.base import BaseCommand

from humans.models import Group


class Command(BaseCommand):
    help = 'random group'

    def add_arguments(self, parser):
        parser.add_argument(
             '--number',
            help='Delete poll instennd of closin it',)

    def handle(self, *args, **options):
        number = int(options.get('number') or 100)
        for _ in range(number):
            Group.generate_group()
