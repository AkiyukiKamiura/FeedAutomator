from flask import Blueprint, jsonify, request, url_for, make_response
from random import *
from flask_cors import CORS

from backend import app, db
from backend.models import Task, Feed, Entry

# 自作ライブラリ
import echo, motto

api = Blueprint('api', __name__)

@api.route('/hello/<string:name>/')
def say_hello(name):
    response = { 'msg': "Hello {}".format(name) }
    return jsonify(response)

@api.route('/feeds/get', methods=['GET'])
def get_feeds():
    feeds = Feed.query.order_by(Feed.id.desc()).all()
    feeds_dict = [feed.to_dict() for feed in feeds]
    return jsonify(feeds_dict)

@api.route('/feeds/<int:id>/entries', methods=['GET'])
def get_entries(id):
    feed = Feed.query.get(id)
    entries = list(map(lambda x: x.to_dict(), list(feed.entries)))
    return jsonify(entries)

@api.route('/wakati', methods=['GET'])
def wakati_text():
    return 'wakati'

@api.route('/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@api.route('/get', methods=['GET'])
def get_task():
    taks = Task.query.order_by(Task.id.desc()).all()
    taks_dict = [task.to_dict() for task in taks]
    return jsonify(taks_dict)

@api.route('/add', methods=['POST'])
def add_task():
    task = Task(
            title=request.form['title'],
            text=request.form['text']
            )
    db.session.add(task)
    db.session.commit()
    task = Task.query.order_by(Task.id.desc()).first()
    id = str(task.id)
    r = make_response(id)
    return r

@api.route('/delete', methods=['POST'])
def delete_task():
    id=request.form['id']
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    r = make_response(id)
    return r
