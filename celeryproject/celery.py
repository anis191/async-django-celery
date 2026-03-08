import os

from celery import Celery
from time import sleep
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryproject.settings')

app = Celery('celeryproject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task
def add(x,y):
    sleep(10)
    return x + y

# Periodic Task:
app.conf.beat_schedule = {
    'clear-session-cache-every-10sec' : {
        'task' : "myapp.tasks.clear_session_cache",
        "schedule": crontab(minute='*/1'),
        'args' : ('11111', )
    }
}