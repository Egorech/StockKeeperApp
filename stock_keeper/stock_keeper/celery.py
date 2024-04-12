from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установите переменную окружения для настроек Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_keeper.settings')

app = Celery('stock_keeper')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение и регистрация задач из файлов tasks.py в приложениях Django
app.autodiscover_tasks()