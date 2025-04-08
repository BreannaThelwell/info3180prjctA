#initial attempt

from flask import flask
from flask_cors import CORS #frontend requests
from flask_jwt_extended import JWTManager #import for token
from flask_sqlalchemy import SQLAlchemy #db import
from flask_migrate import Migrate #db import
from views.auth import auth_bp #bp import
from views.user import user_bp #bp import
from views.profile import profile_bp #bp import
from .config import Config #app config file

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

#initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app,db)

#register bps (blueprints)
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(profile_bp)