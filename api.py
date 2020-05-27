"""
module api contains a flask app with a single endpoint.
"""
import json
import logging
import os
from datetime import datetime
from flask import Flask, request


app = Flask(__name__)
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    """
    The "Hello, World" endpoint that handles GET and POSTS requests.
    This function will check the requests headers for 'Accept' and determine
    whether to return an HTML string or JSON.
    """
    if os.environ.get('DEBUG'):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger.debug(f'{timestamp} - {request.url}')

    if request.headers.get('Accept') == 'application/json':
        return {'message': 'Hello, World'}
    return '<p>Hello, World</p>'


if __name__ == '__main__':
    app.run()