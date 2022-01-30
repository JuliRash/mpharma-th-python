import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mpharma_python.settings')

app = Celery('mpharma_python')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
