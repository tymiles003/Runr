#http://legacy.python.org/dev/peps/pep-0420/
from flask import Flask

def create_app(config_name=''):
    app = Flask(__name__)

    return app