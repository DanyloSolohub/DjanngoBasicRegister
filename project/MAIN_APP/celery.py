import logging
import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MAIN_APP.settings')

celery_app = Celery('MAIN_APP')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks()


@celery_app.task
def test_task():
    logging.warning('test task')


@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        1, test_task.s()
    )
