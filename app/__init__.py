#initial attempt

from flask import Flask
from flask_cors import CORS #frontend requests
from app.extensions import db, jwt, migrate #extensions import
from .views.auth import auth_bp #bp import
from .views.user import user_bp #bp import
from .views.profile import profile_bp #bp import
from .config import Config #app config file


def create_app():  #avoiding circular import
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    
    #initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app,db)
    
    #register bps (blueprints)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(profile_bp)
    
    return app