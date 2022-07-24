from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
# from django_celery_beat.models import PeriodicTasks
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app = Celery('django_celery')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# CELERY BEAT SETTINGS
app.conf.beat_schedule = {
    'send-mail-everyday-at-8': {
        'task': 'send_email.tasks.send_email',
        'schedule': crontab(hour=18, minute=5),
        # 'schedule': crontab(hour=18, minute=5, day_of_month=, day_of_year=,), # runs only once with all detail
        # 'args': (2, ) 
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')