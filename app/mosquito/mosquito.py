from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
mongo = MongoClient('mongodb://root:pass@mongo')
db = mongo.mosquito


@app.route('/active')
def active():
    active = db.active.find()
    print(active)
    return {
        'result': [{'name': user['name']} for user in active]
    }
