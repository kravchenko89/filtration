from __future__ import absolute_import, unicode_literals

from celery import shared_task, task

from django.core.mail import send_mail

from .models import Logger
from datetime import datetime, timedelta, timezone


@shared_task
def task_email_send(subject, message, email_from,
                    recipient_list):
    send_mail(subject, message, email_from,
              recipient_list,
              fail_silently=False)


@task()
def task_clean():

    Logger.objects.filter(created__lte=datetime.now(tz=timezone.utc) - timedelta(days=7)).delete()

    # time_now = datetime.now(tz=timezone.utc)  # без tz нельзя сравнивать относительное и абсолютное время
    # for logger in Logger.objects.all():
    #     if logger.created < time_now - timedelta(days=7):
    #         # breakpoint()
    #         logger.delete()

