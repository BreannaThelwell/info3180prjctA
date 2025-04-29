#being used to avoid circular import

from flask_sqlalchemy import SQLAlchemy #db import
from flask_jwt_extended import JWTManager #token import
from flask_migrate import Migrate #db import

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()
