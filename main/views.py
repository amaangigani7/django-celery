import json
from django.shortcuts import render
from django.http import HttpResponse
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from .tasks import test_func

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("done")


def send_mail_to_all(request):
    from send_email.tasks import send_email

    send_email.delay()
    return HttpResponse('sent')


def schedule_email(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=18, minute=34)
    task = PeriodicTask.objects.create(crontab=schedule, name='schedule_mail_'+'1', task='send_email.tasks.send_email', args=json.dumps((2, 3)))
    return HttpResponse('sent')