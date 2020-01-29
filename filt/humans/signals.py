from django.db.models.signals import pre_save
from django.dispatch import receiver

from humans.models import Teacher, Student


@receiver(pre_save, sender=Teacher)
def pte_save_teacher(sender, instance, **kwargs):
    instance.email = instance.email.lower()


@receiver(pre_save, sender=Teacher)
def pte_save_teacher(sender, instance, **kwargs):
    instance.phone = int(instance.phone)


@receiver(pre_save, sender=Teacher)
def pte_save_teacher(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()


@receiver(pre_save, sender=Teacher)
def pte_save_teacher(sender, instance, **kwargs):
    instance.last_name = instance.last_name.capitalize()


@receiver(pre_save, sender=Student)
def pte_save_student(sender, instance, **kwargs):
    instance.email = instance.email.lower()


@receiver(pre_save, sender=Student)
def pte_save_student(sender, instance, **kwargs):
    instance.phone = int(instance.phone)


@receiver(pre_save, sender=Student)
def pte_save_student(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()


@receiver(pre_save, sender=Student)
def pte_save_student(sender, instance, **kwargs):
    instance.last_name = instance.last_name.capitalize()
