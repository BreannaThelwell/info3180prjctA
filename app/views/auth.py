#initial attempt
#using flask blueprint to help flesh out the reusable components of app instead 
#of having it all in one file. by splitting it like this, it helps with keeping
#modules/logic separate, and helps with maintainability and scalability.

#this file handles user registration, login, and logout 

#imports 
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db, User
import datetime

auth_bp = Blueprint('auth', __name__) #creating bp

#route for registering as a new user
@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
   #check if username already exists 
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'msg': 'Username already exists'}), 400
    #hash password
    hashed = generate_password_hash(data['password'])
    #creating new user
    new_user = User(
        username=data['username'],
        password=hashed,
        name=data['name'],
        email=data['email'],
        photo=data['photo'],
        date_joined=datetime.datetime.utcnow()
    )
    db.session.add(new_user) #adds newly registered user's info to db
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201 

    #route for user login and jwt token generation
@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first() #queries db
        #validation
        if not user or not check_password_hash(user.password, data['password']):
            return jsonify({"message": "Invalid username or password"}), 401
        access_token = create_access_token(identity=user.id)
        return jsonify({"token": access_token, "user_id": user.id}), 200

    #protected logout route
@auth_bp.route('/api/auth/logout', methods=['POST'])
@jwt_required()
def logout():
        #confirm end of session on client side
        return jsonify({"message": "User logged out successfully"}), 200