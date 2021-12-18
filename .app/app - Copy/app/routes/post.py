from app import app


@app.route('/post/<string:msg>')
def post_task(msg):
    from app.tasks.tasks import task_post
    task_post.apply_async(args=[msg], ignore_result=True)
    return 'please wait...'
