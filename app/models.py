#http://vikku.info/programming/google-maps-v3/draggable-directions/saving-draggable-directions-saving-waypoints-google-directions-google-maps-v3.htm
from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    
    def __repr__(self):
        return '<User {}>'.format(self.username)