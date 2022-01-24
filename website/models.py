from website import db 
from flask_login import UserMixin
from sqlalchemy.sql import func # from string current time
 
class Rooms(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    roomno = db.Column(db.String(150), unique = True)
    homie = db.Column(db.Integer, db.ForeignKey('user.id'), default= None) # Creates a one to many relationship i.e one user -> many rooms ... many more relationships can exist
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    rollno = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    phoneno = db.Column(db.String(10))
    isAlotted = db.Column(db.Boolean(), default = False)
    rooms = db.relationship('Rooms')
    
    