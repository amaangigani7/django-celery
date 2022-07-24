from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task(bind=True)
def send_email(self, *args):
    users = get_user_model().objects.all()
    for user in users:
        email = user.email
        subject = 'hi'
        message = 'testing'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,]
        send_mail(subject, message, email_from, recipient_list, fail_silently=True)
    return 'Done'