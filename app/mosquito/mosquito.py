from flask import Flask

app = Flask(__name__)


@app.route('/')
def register():
    return {
        'status': 'ok'
    }
