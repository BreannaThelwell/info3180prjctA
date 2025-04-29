from app.extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash  
from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(100), nullable=False)  
    email = db.Column(db.String(120), unique=True, nullable=False)  
    photo = db.Column(db.String(200))  
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)  
    
    
    profiles = db.relationship('Profile', backref='user', lazy=True)
    favorites = db.relationship('Favourite', foreign_keys='Favourite.user_id', backref='favoriter', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.Text)
    parish = db.Column(db.String(50))
    biography = db.Column(db.Text)
    sex = db.Column(db.String(10))
    race = db.Column(db.String(50))
    birth_year = db.Column(db.Integer)
    height = db.Column(db.Float) 
    fav_cuisine = db.Column(db.String(50))
    fav_colour = db.Column(db.String(50))
    fav_school_subject = db.Column(db.String(50)) 
    political = db.Column(db.Boolean)
    religious = db.Column(db.Boolean)
    family_oriented = db.Column(db.Boolean)
    
class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id_fk = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    fav_user_id_fk = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    __table_args__ = (db.UniqueConstraint('user_id_fk', 'fav_user_id_fk', name='unique_favorite'),)