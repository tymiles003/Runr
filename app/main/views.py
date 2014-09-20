from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from ..models  import User

@main.route('/', methods=['GET', 'POST'])
def index():
    users = User.query.all()    
    return render_template('base.html', users=users)