import random

from django.core.management.base import BaseCommand

from humans.models import Group, Teacher, Student


class Command(BaseCommand):
    help = 'random group'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            help='Delete poll instennd of closin it',)

    def handle(self, *args, **options):
        # Group.objects.all().delete()
        # pdb.set_trace()
        curators = []   # Teacher
        headmans = []   # Student
        print(curators)
        for _ in range(10):
            curators.append(Teacher.generate())
            headmans.append(Student.generate())

        number = int(options.get('number') or 100)
        for _ in range(number):
            group = Group.generate()
            group.curratt = random.choice(curators)
            group.headman = random.choice(headmans)
            group.save()
