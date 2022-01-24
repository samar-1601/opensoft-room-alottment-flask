# stores views/ urls for the website
from flask import Blueprint, render_template, request
from flask.helpers import flash
from flask.json import jsonify # way to organise files
from flask_login import login_required, current_user
from .models import Note, db, Rooms, User
# from website.auth import login
import json

views = Blueprint('views', __name__)

# @views.route('/', methods=['GET', 'POST'])
# def house():
#     if request.method=='GET':
#      return 
 
@views.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    # print("inside home-----------------")
    # if request.method == 'POST':
    #     note = request.form.get('note')
        
    #     if len(note) < 1:
    #         flash('Note is too short !!')
    #     else:
    #         new_note = Note(data = note, user_id = current_user.id)
    #         db.session.add(new_note)
    #         db.session.commit()
    #         flash('Note Entered Successfully !!')
    print("----- Inside Home function ----")
    rooms = Rooms.query.filter(Rooms.homie != None).all()
    roomList = {}
    for aroom in rooms:
        boarder = User.query.filter(User.id==aroom.homie).first()
        roomList[aroom.roomno] = [boarder.name, boarder.rollno]
    print(roomList)  
    return render_template("home.html", user = current_user, roomList = roomList)

@views.route('/delete-note', methods = ['POST'])
@login_required
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})

@views.route('/allot-room', methods = ['POST'])
@login_required
def allot_room():
    print("----- Inside Allot-Room function ----")
    room = json.loads(request.data)
    print(room)
    roomId = room['roomId']
    print("roomId we got : ") 
    print(roomId)
    room = Rooms.query.filter_by(roomno = int(roomId)).first()
    print("room Details : ")
    print(room)
    room.homie = current_user.id
    current_user.isAlotted = True
    db.session.commit()
    print("updated room : ")
    print(room)
    print(room.homie)
    print("Room Boarder ") 
    print(current_user)
    print(current_user.rooms[0].roomno)
    rooms = Rooms.query.filter(Rooms.homie != None).all()
    roomList = {}
    for aroom in rooms:
        boarder = User.query.filter(User.id==aroom.homie).first()
        roomList[aroom.roomno] = [boarder.name, boarder.rollno]
    print(roomList)  
    return render_template("home.html", user = current_user, roomList = roomList)

