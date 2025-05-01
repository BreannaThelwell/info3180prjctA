#initial attempt
#using flask blueprint to help flesh out the reusable components of app instead 
#of having it all in one file. by splitting it like this, it helps with keeping
#modules/logic separate, and helps with maintainability and scalability.

#this file handles all profile related functions such as:
#getting all profiles on system, creating one, view full profile details,
#add one to "favourites", matches criteria, and searches

#imports
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Profile, User, Favourite
from sqlalchemy import func
from datetime import datetime

profile_bp = Blueprint('profile', __name__) #creating bp

#route to GET all profiles in the system
#returns all profiles in search except current user
@profile_bp.route('/api/profiles', methods=['GET'])
@jwt_required()
def get_profiles():
    current_user = int(get_jwt_identity())
    profiles = Profile.query.filter(Profile.user_id_fk != current_user).all()
    return jsonify([p_to_dict(p) for p in profiles])

#helper method
def p_to_dict(p):
    return {
        'id': p.id,
        'user_id': p.user_id_fk,
        'description': p.description,
        'parish': p.parish,
        'biography': p.biography,
        'sex': p.sex,
        'race': p.race,
        'birth_year': p.birth_year,
        'height': p.height,
        'fav_cuisine': p.fav_cuisine,
        'fav_colour': p.fav_colour,
        'fav_school_subject': p.fav_school_subject,
        'political': p.political,
        'religious': p.religious,
        'family_oriented': p.family_oriented
    }

#create a new profile 
@profile_bp.route('/api/profiles', methods=['POST'])
@jwt_required()
def add_profile():
    data = request.get_json()
    user_id = int(get_jwt_identity())
    new_profile = Profile(user_id_fk=user_id, **data)
    db.session.add(new_profile)
    db.session.commit()
    return jsonify({"message": "Profile created"}), 201

#GET full profile details by id
@profile_bp.route('/api/profiles/<int:profile_id>', methods=['GET'])
@jwt_required()
def get_profile_details(profile_id):
    profile = Profile.query.get_or_404(profile_id)
    return jsonify(p_to_dict(profile))

#add profile/user to favourites
@profile_bp.route('/api/profiles/<int:user_id>/favourite', methods=['POST'])
@jwt_required()
def add_to_favourites(user_id):
    current_user_id = int(get_jwt_identity())
    #check if the user being favourited exists
    target_user = User.query.get(user_id)
    if not target_user:
        return jsonify({"error": "User to be favourited does not exist"}), 404

    #then add to favourite
    fav = Favourite(user_id_fk=current_user_id, fav_user_id_fk=user_id)
    db.session.add(fav)
    db.session.commit()
    return jsonify({"message": "User added to favourites"}), 201

#GET list of profiles that match criteria
#filtered by: exclude self, age range within 5 years, height difference 3-10 inches, at least 3 of 6 fields
@profile_bp.route('/api/profiles/matches/<int:profile_id>', methods=['GET'])
@jwt_required()
def get_matches(profile_id):
    current_profile = Profile.query.get_or_404(profile_id)
    all_profiles = Profile.query.filter(Profile.id != profile_id).all()
    matched_profiles = []
        
    for p in all_profiles:
        age_diff = abs(current_profile.birth_year - p.birth_year)
        height_diff = abs(current_profile.height - p.height)
        match_fields = sum([
            current_profile.fav_cuisine == p.fav_cuisine,
            current_profile.fav_colour == p.fav_colour,
            current_profile.fav_school_subject == p.fav_school_subject,
            current_profile.political == p.political,
            current_profile.religious == p.religious,
            current_profile.family_oriented == p.family_oriented
        ])
        if age_diff <= 5 and 3 <= height_diff <= 10 and match_fields >= 3:
            matched_profiles.append(p.serialize())
    return jsonify(matched_profiles), 200

#search for profiles based on name, birth year, sex, and race
@profile_bp.route('/api/search', methods=['GET'])
@jwt_required()
def search_profiles():
    name = request.args.get('name')
    birth_year = request.args.get('birth_year')
    sex = request.args.get('sex')
    race = request.args.get('race')
    current_user_id = get_jwt_identity()

    query = Profile.query.join(User).filter(User.id != current_user_id)

    if name:
        query = query.filter(User.name.ilike(f"%{name}%"))
    if birth_year:
        query = query.filter(Profile.birth_year == int(birth_year))
    if sex:
        query = query.filter(Profile.sex == sex)
    if race:
        query = query.filter(Profile.race == race)

    results = query.all()
    return jsonify([p.serialize() for p in results]), 200



