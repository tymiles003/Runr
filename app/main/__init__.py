from flask import Blueprint

main = Blueprint('main', __name__)

#Avoid circular dependency by importing the following files after the main declaration
from . import views
from . import errors