from flask import Flask
from flask_migrate import Migrate
from app.config import DevelopmentConfig
from app.extensions import db
from app.models.user import User
from app.models.task import Task
from app.models.ai_job import AIJob
from app.models.ai_analysis_result import AIAnalysisResult
from app.models.ai_analysis_history import AIAnalysisHistory
from app.routes.main import main
from app.routes.users import users
from app.routes.auth import auth

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    Migrate(app, db)
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(auth)
    return app
