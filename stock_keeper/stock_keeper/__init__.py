from __future__ import absolute_import, unicode_literals

# Это позволит убедиться, что приложение всегда импортируется, когда запускается Django
from stock_keeper.celery import app as celery_app

__all__ = ('celery_app',)
