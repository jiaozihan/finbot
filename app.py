from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/event')
def response_event():
    request_json = request.get_json()
    return request_json['challenge']
