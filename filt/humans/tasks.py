from celery import shared_task
from django.core.mail import send_mail


@shared_task
def task_email_send(subject, message, email_from,
                    recipient_list):
    send_mail(subject, message, email_from,
              recipient_list,
              fail_silently=False)
