from flask import Flask
from app.config import DevelopmentConfig
from app.extensions import db
from app.models.user import User
from app.routes.main import main
from app.routes.users import users
from app.routes.auth import auth

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(auth)
    return app
