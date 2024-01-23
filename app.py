from flask import Flask, request
import db
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return 'Hi, World!'

@app.route("/posts.json")
def index():
    return db.posts_all()

@app.route("/posts.json", methods=["POST"])
def create():
    user_id = request.form.get("user_id")
    title = request.form.get("title")
    body = request.form.get("body")
    return db.posts_create(user_id, title, body)

@app.route("/posts/<id>.json")
def show(id):
    return db.posts_find_by_id(id)


@app.route("/posts/<id>.json", methods=["PATCH"])
def update(id):
    user_id = request.form.get("user_id")
    title = request.form.get("title")
    body = request.form.get("body")
    return db.posts_update_by_id(id, user_id, title, body)

@app.route("/posts/<id>.json", methods=["DELETE"])
def destroy(id):
    return db.posts_destroy_by_id(id)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"