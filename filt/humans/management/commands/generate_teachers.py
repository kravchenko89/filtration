from django.core.management.base import BaseCommand

from humans.models import Teacher


class Command(BaseCommand):
    help = 'random teachers'

    def add_arguments(self, parser):
        parser.add_argument(
             '--number',
            help='Delete poll instennd of closin it',
        )

    def handle(self, *args, **options):
        number = int(options.get('number') or 100)
        for _ in range(number):
            Teacher.generate_teacher()
