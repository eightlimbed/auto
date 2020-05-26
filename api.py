"""
module api contains a flask app with a single endpoint.
"""
import json
from flask import Flask, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.headers.get('Accept') == 'application/json':
        return {'message': 'Hello, World'}
    return '<p>Hello, World</p>'

if __name__ == '__main__':
    app.run()