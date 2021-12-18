from app import app, db

@app.route("/")
def hello():
    db.create_all()
    return "Hello, Flask!"
