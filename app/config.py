#initial attempt

import os #required import
import dotenv import load_dotenv #required import

load_dotenv()  #load environment variables from .env

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', '$ec5etK*y')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'Sup3r$3cRe1k*Y')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://') #if we're using postgresql
    SQLALCHEMY_TRACK_MODIFICATIONS = False #here to suppress warning from SQLAlchemy 