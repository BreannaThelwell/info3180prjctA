#initial attempt
#using flask blueprint to help flesh out the reusable components of app instead 
#of having it all in one file. by splitting it like this, it helps with keeping
#modules/logic separate, and helps with maintainability and scalability.

#this file handles all user related functions such as:
#getting details about a specific user, user's favourites, user's top favorites

#imports
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, User, Profile, Favourite
from sqlalchemy import func
from datetime import datetime 

user_bp = Blueprint('user', __name__) #creating bp

#GET details about user and their profile
@user_bp.route('/api/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_details(user_id):
    user = User.query.get_or_404(user_id)
    profiles = Profile.query.filter_by(user_id=user_id).all()
    #return limited for privacy/security and performance 
    return jsonify({
        'id': user.id,
        'username': user.username,
        'name': user.name,
        'email': user.email,
        'photo': user.photo,
        'profiles': [{
            'id': p.id, 'description': p.description
        } for p in profiles]
    })

#GET all users from favourites
@user_bp.route('/api/users/<int:user_id>/favourites', methods=['GET'])
@jwt_required()
def get_user_favourites(user_id):
    favs = Favourite.query.filter_by(user_id=user_id).all()
    results = []
    for f in favs:
        u = User.query.get(f.fav_user_id)
        if u:
            results.append({'id': u.id, 'name': u.name})
    return jsonify(results) 

#GET top n favoured users system-wide
#restricted to logged-in users
@user_bp.route('/api/users/favourites/<int:n>', methods=['GET'])
@jwt_required()
def top_favourites(n):
    top_fav_ids = db.session.query(
        Favourite.fav_user_id, func.count().label('fav_count')
    ).group_by(Favourite.fav_user_id).order_by(func.count().desc()).limit(n).all()

    results = []
    for user_id, count in top_fav_ids:
        user = User.query.get(user_id)
        if user:
            results.append({'id': user.id, 'name': user.name, 'count': count})
    return jsonify(results)