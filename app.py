"""
Author : Kartikeyan Gupta,
         Manmeet Gandhi
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import os
from config import *
from models import *

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


@app.route('/add/user/', methods=['POST'])
def add_user():
    """
       Usercase : Add a user in Database
       Roles: AdminOnly
       Method: Post
       Params : name, password, is_Admin
    """
    try:
        if request.method == 'POST':
            data = request.get_json()
            role_id = Role.query.filter_by(name='User').first().id
            if data['isAdmin']:
                role_id = Role.query.filter_by(name='Admin').first().id
            new_user = User(name=data['username'], password=data['password'], role_id=role_id)
            db.session.add(new_user)
            db.session.commit()
            code, msg, result = 200, "user {} created".format(data['username']), True
    except Exception as e:
        code, msg, result = 500, "Error occoured {}".format(type(e).__name__), False
    return jsonify({"result": result, 'message':msg}), code


@app.route('/add/train/', methods=['POST'])
def add_train():
    """
       Usercase : Add a train in Database
       Roles: AdminOnly
       Method: Post
       Params : name
    """
    try:
        if request.method == 'POST':
            data = request.get_json()
            new_train = Train(name=data['name'])
            db.session.add(new_train)
            db.session.commit()
            code, msg, result = 200, "New Train {} Added".format(data['name']), True
    except Exception as e:
        code, msg, result = 500, "Error occoured {}".format(type(e).__name__), False
        code = 500
        result = False   
    return jsonify({"result": result, 'message':msg}), code


@app.route('/add/train_coach/', methods=['POST'])
def add_train_coach():
    """
       Usercase : Add a Coach for a specific train in Database
       Roles: AdminOnly
       Method: Post
       Params : TrainName, CoachName
    """
    try:
        if request.method == 'POST':
            data = request.get_json()
            train_id = Train.query.filter_by(name=data["trainName"]).first().id
            coach_id = Coach.query.filter_by(name=data["coachName"]).first().id
            new_data = TrainCoach(train_id=train_id, coach_id=coach_id)
            db.session.add(new_data)
            db.session.commit()
            code, msg, result = 200, "New coach {} added in train {} ".format(data['trainName'], data['coachName']), True
    except Exception as e:
        code, msg, result = 500, "Error occoured {}".format(type(e).__name__), False
    
    return jsonify({"result": result, 'message':msg}), code

@app.route('/remove/train_coach/', methods=['DELETE'])
def delete_train_coach():
    """
       Usercase : Remove a Coach for a specfic train in Database
       Roles: AdminOnly
       Method: Delete
       Params : id<Integer>
    """
    try:
        if request.method == 'DELETE':
            data = request.get_json()
            # train_id = Train.query.filter_by(name=data["trainName"]).first().id
            # coach_id = Coach.query.filter_by(name=data["coachO"]).first().id
            # train_coach_id = TrainCoach.filter_by(train_id=train_id, coach_id=coach_id).first().id()
            
            d = db.session.query(TrainCoach).filter(TrainCoach.id==data["trainCoachId"]).first()
            db.session.delete(d)
            db.session.commit()
            code, msg, result = 200, "coach-id {} deleted ".format(data["trainCoachId"]), True
    except Exception as e:
        code, msg, result = 500, "Error occoured {}".format(type(e).__name__), False
    
    return jsonify({"result": result, 'message':msg}), code

@app.route('/add/booking/', methods=['POST'])
def add_booking():
    """
       Usercase : Add a booking in Database
       Roles: all
       Method: Post
       Params : TrainName, CoachName, username
    """
    try:
        result = False
        msg = "Error"
        code = 500
        if request.method == 'POST':
            data = request.get_json()
            train_id = Train.query.filter_by(name=data["trainName"]).first().id
            coach_id = Coach.query.filter_by(name=data["coachName"]).first().id
            user_id = User.query.filter_by(name=data["username"]).first().id
            flag=0
            index=0
            train_coach_ids = TrainCoach.query.filter_by(train_id=train_id, coach_id=coach_id).all()
            while flag !=1 :
                if len(train_coach_ids) == 0:
                    code, msg, result = 200, "Train {} with coach {} Doesn't Exist".format(data["trainName"], data["coachName"]), True
                    flag=1
                elif index >= len(train_coach_ids):
                    code, msg, result = 200, "Train Full booked", False
                    flag=1
                else:
                    train_coach_id = train_coach_ids[index].id 
                    seats_booked = len(Booking.query.filter_by(train_coach_id=train_coach_id).all())
                    if seats_booked < Coach.query.filter_by(name=data["coachName"]).first().total_seats:
                        new_booking = Booking(train_coach_id=train_coach_id, user_id=user_id, seat_number=seats_booked+1)        
                        db.session.add(new_booking)
                        db.session.commit()
                        code, msg, result = 200, "Seat booked at train {}, Coach {}, Seat Number {}".format(data["trainName"], data["coachName"], seats_booked+1), True
                        flag=1
                    else:
                        index+=1
    except Exception as e:
        code, msg, result = 500, "Error occoured {}".format(type(e).__name__), False
    
    return jsonify({"result": result, 'message':msg}), code

@app.route('/get/booking/', methods=['POST'])
def get_booking():
    """
       Usercase : Get all booking in Database
       Roles: all
       Method: Get
       Params : None
    """
    try:
        result = False
        msg = "Error"
        code = 500
        bookings = Booking.query.all()
        data = []
        for booking in bookings:
            id = booking.id
            train_name = Train.query.filter_by(id=TrainCoach.query.filter_by(id=booking.train_coach_id).first().train_id).first().name
            coach_name = Coach.query.filter_by(id=TrainCoach.query.filter_by(id=booking.train_coach_id).first().coach_id).first().name
            seat_number = booking.seat_number
            username = User.query.filter_by(id=booking.user_id).first().name
            bookdata = {
                "id": id,
                "train_name": train_name,
                "coach_name": coach_name,
                "seat_number": seat_number,
                "username": username  
            }
            data.append(bookdata)
        code, msg, result = 200, data, True
        
    except Exception as e:
        code, msg, result = 500, "Error occoured {}".format(type(e).__name__), False
    
    return jsonify({"result": result, 'message':msg}), code


# Error handlers.
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'result': False, "message": "Internal Server error"}), 500


@app.errorhandler(404)
def not_found(error):
    return jsonify({'result': False, "message": "API doesn't exist"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # 127.0.0.1
