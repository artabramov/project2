from .. import make_celery
from .. import db
from ..models import msg

celery = make_celery()

@celery.task(name='post.post_msg')
def post_msg(tmp):
    obj = msg.Msg(msg=tmp)
    db.session.add(obj)
    db.session.commit()
    return 'success'
