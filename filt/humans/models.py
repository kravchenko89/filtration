from faker import Faker
import random

from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    lesson = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    credit_card = models.CharField(max_length=255, null=True, blank=True)

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
            lesson=random.choice(['Math', 'Physics', 'History', 'Language']),
            birth_date=fake.date_object(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            credit_card=fake.credit_card_number(card_type=None)
        )
        teacher.save()
        return teacher

    def __str__(self):
        return f'{self.id} {self.full_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Group(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    curratt = models.ForeignKey('humans.Teacher', null=True, blank=True, on_delete=models.CASCADE)
    headman = models.ForeignKey('humans.Student', null=True, blank=True, on_delete=models.CASCADE)

    def get_info(self):
        return f'Curator:: {self.curratt} | Headman:: {self.headman} | Group:: {self.name}'

    @classmethod
    def generate_group(cls):
        faker = Faker()
        group = cls(
            name=faker.word()
        )
        group.save()
        return group

    def __str__(self):
        return f'{self.id}  {self.curratt} {self.headman}'


class Student(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    address = models.CharField(max_length=255, null=True, blank=True)
    groupp = models.ForeignKey('humans.Group', null=True, blank=True, on_delete=models.CASCADE)

    def get_info(self):
        return f'Student:: {self.first_name} {self.last_name} | Phone'

    @classmethod
    def generate_student(cls):
        faker = Faker()
        student = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            phone=faker.phone_number(),
            email=faker.email(),
            address=faker.address(),
        )
        student.save()
        return student

    def __str__(self):
        return f'{self.id} {self.full_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
