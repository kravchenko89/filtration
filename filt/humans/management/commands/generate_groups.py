import random
import re

from django.core.management.base import BaseCommand

from humans.models import Teacher, Student, Group


class Command(BaseCommand):
    help = 'random teachers'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            help='Delete poll instennd of closin it',)

    def handle(self, *args, **options):

        curators = []   # Teacher
        groups = []

        for i in range(20):
            groups.append(Group.generate_group())
            curators.append(Teacher.generate_teacher())

        for teacher in Teacher.objects.all():
            teacher.phone = re.sub("\D", "", teacher.phone)
            teacher.save()

        students = list(Student.objects.all())
        for group in Group.objects.all():
            group.headman = random.choice(students)
            group.curratt = random.choice(curators)
            group.save()

        for student in Student.objects.all():
            student.groupp = random.choice(groups)
            student.save()
