from __future__ import absolute_import, unicode_literals

from kombu.utils.url import safequote

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vimansathi.settings')
app = Celery('vimansathi')
# app.conf.broker_read_url = 'redis://viman-ro.hmguvw.ng.0001.aps1.cache.amazonaws.com:6379'
app.conf.broker_url = 'redis://127.0.0.1:6379'
# app.conf.broker_url = 'redis://viman-001.hmguvw.0001.aps1.cache.amazonaws.com:6379'
                                    
                           
#this 
# app.conf.result_backend = 'redis://viman-001.hmguvw.0001.aps1.cache.amazonaws.com:6379/0'
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'display_time-30-seconds': {
        'task': 'demoapp.tasks.display_time',
        'schedule': 10.0
    },
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


