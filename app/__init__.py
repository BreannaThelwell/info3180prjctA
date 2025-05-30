#initial attempt

import os
from flask import Flask
from flask import send_from_directory, request #npm run build import
from flask_cors import CORS #frontend requests
from app.extensions import db, jwt, migrate #extensions import
from .views.auth import auth_bp #bp import
from .views.user import user_bp #bp import
from .views.profile import profile_bp #bp import
from .config import Config #app config file


def create_app():  #avoiding circular import
    app = Flask(__name__, static_url_path='', static_folder='static')
    #allow methods and headers
    CORS(app, resources={r"/api/*": {"origins": [ "http://localhost:5173","https://jamdate-xe9i.onrender.com"] }}, supports_credentials=True)

    app.config['UPLOAD_FOLDER'] = './uploads'
    app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

    app.config.from_object(Config)
    
    #initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app,db)
    
    #register bps (blueprints)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(profile_bp)

    #uploads
    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    #for render testing to serve static frontend
    @app.route('/')
    @app.route('/<path:path>')
    def serve_vue_app(path=''):
        if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
            return send_from_directory(app.static_folder, path)
        else:
            return send_from_directory(app.static_folder, 'index.html')

    return app

   