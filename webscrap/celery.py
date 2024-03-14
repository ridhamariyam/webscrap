from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from datetime import timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webscrap.settings')

app = Celery('webscrap')

app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object('django.conf:settings', namespace='CELERY')

#celery beat settings

app.conf.beat_schedule = {
    'scrape-proxy-list-every-24-hours': {
        'task': 'proxyapp.tasks.scrape_proxy_list',
        'schedule': timedelta(hours=24),
    },
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')



