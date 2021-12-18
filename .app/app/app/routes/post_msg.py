from flask import jsonify
from app import app

@app.route('/post_msg/<string:msg>')
def async_job(msg):
    from app.tasks.post_msg import post_msg

    result = post_msg.apply_async(args=[msg], ignore_result=True)

    return jsonify('post_msg... result: ' + str(result))
