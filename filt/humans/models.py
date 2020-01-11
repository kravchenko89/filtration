from faker import Faker
import random

from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True, blank=True)
    lesson = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=255, null=True, blank=True)
    credit_card = models.CharField(max_length=20, null=True, blank=True)

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.birth_date}' \
               f' {self.email} {self.country} {self.lesson}'

    @classmethod
    def generate_teacher(cls):
        fake = Faker()
        teacher = cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            country=fake.country(),
            lesson=random.choice(['math', 'physics', 'history', 'language']),
            birth_date=fake.date_object(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            credit_card=fake.credit_card_number(card_type=None)
        )
        teacher.save()
        return teacher


class Group(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    lesson = models.CharField(max_length=100)
    curator = models.CharField(max_length=100, null=True, blank=True)
    group = models.CharField(max_length=20)
    phone = models.CharField(max_length=16)

    def get_info(self):
        return f'Student:: {self.first_name} {self.last_name} | Group:: {self.group}' \
               f' lessons:: {self.lesson} | Curator:: {self.curator} | Phone:: {self.phone}'

    @classmethod
    def generate_group(cls):
        faker = Faker()
        less = ['Math', 'Physics', 'History',
                'Language', 'Management', 'Python']
        group = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            lesson=random.choice(less),
            curator=faker.name(),
            group=random.randint(1, 20),
            phone=faker.phone_number(),
        )
        group.save()
        return group
