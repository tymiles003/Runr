#http://legacy.python.org/dev/peps/pep-0420/
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    
    #Extra stuff here: Attach routes and custom pages
    #Imports are always interpreted as absolute, hence the need for the '.' below.
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app