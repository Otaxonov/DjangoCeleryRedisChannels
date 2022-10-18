import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DCRCH.settings')

app = Celery('DCRCH')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_jokes_3s': {
        'task': 'Jokes.tasks.get_joke',
        'schedule': 3.0,
    },
}

app.autodiscover_tasks()