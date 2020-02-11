import re

from django.core.management.base import BaseCommand

from humans.models import Teacher, Student


class Command(BaseCommand):
    help = 'random teachers'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            help='Delete poll instennd of closin it', )

    def handle(self, *args, **options):
        # Перебрал все номера и убрал символы
        for student in Student.objects.all():
            student.phone = re.sub("\D", "", student.phone)
            student.save()

        for teacher in Teacher.objects.all():
            teacher.phone = re.sub("\D", "", teacher.phone)
            teacher.save()
