from app import make_celery

celery = make_celery()

@celery.task(value='web.post')
def task_post(msg):
    import time
    time.sleep(30)
    return None


"""
from celery import Celery

celery = Celery('tasks', broker='amqp://guest:guest@host.docker.internal:5672//', backend='rpc://')
celery.conf.task_default_queue = 'default'

@celery.task
def task_post(msg):
    #import time
    #time.sleep(30)
    return None
"""
