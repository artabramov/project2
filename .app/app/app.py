from flask import Flask, jsonify, request
from celery import Celery

app = Flask(__name__)
app.debug = True
app.config['CELERY_BROKER_URL'] = 'amqp://guest:guest@host.docker.internal:5672//'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'

# где celery будет искать задачи
CELERY_TASK_LIST = [
    'app.tasks'
]

def make_celery():
    celery = Celery(
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_RESULT_BACKEND'],
        include=CELERY_TASK_LIST,
    )

    # какие задачи в какие очереди нужно складывать
    celery.conf.task_routes = {
        'web.*': {'web'},
    }

    # переопределяем класс Task чтобы задачи Celery
    # выполнялись в контексте Flask-приложения
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


@app.route('/')
def hello():
    import sys
    output = '<h1>Hello, Flask!</h1>'
    output += 'APP: ' + str(sys.version_info) + '<br>' + str(sys.path) + '<br>' + str(sys.modules.keys()) + '<br>'
    output += 'REQUEST: ' + str(request.args) + '<br>'
    return output


@app.route('/post/<string:msg>')
def post_task(msg):
    from tasks import task_post
    task_post.apply_async(args=[msg], ignore_result=True)
    return jsonify('please wait...')
