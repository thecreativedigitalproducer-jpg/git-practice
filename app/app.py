from flask import Flask
from app.routes.main import main
from app.routes.users import users

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(users)
    return app
