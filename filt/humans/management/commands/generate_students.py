from django.core.management.base import BaseCommand

from humans.models import Student, Teacher, Group


class Command(BaseCommand):
    help = 'random teachers'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            help='Delete poll instennd of closin it',)

    def handle(self, *args, **options):
        Group.objects.all().delete()
        Teacher.objects.all().delete()
        Student.objects.all().delete()

        number = int(options.get('number') or 100)
        for _ in range(number):
            Student.generate_student()
