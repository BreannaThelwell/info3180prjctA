from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

#db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
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
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'email': self.email,
            'photo': self.photo,
            'date_joined': self.date_joined.isoformat()
        }

class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    user_id_fk = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(200))
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

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id_fk,
            'description': self.description,
            'parish': self.parish,
            'biography': self.biography,
            'sex': self.sex,
            'race': self.race,
            'birth_year': self.birth_year,
            'height': self.height,
            'fav_cuisine': self.fav_cuisine,
            'fav_colour': self.fav_colour,
            'fav_school_subject': self.fav_school_subject,
            'political': self.political,
            'religious': self.religious,
            'family_oriented': self.family_oriented
        }
    
class Favourite(db.Model):
    __tablename__ = 'favourite'
    id = db.Column(db.Integer, primary_key=True)
    user_id_fk = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    fav_user_id_fk = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)