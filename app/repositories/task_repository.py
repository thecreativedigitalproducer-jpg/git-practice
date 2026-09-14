from app.extensions import db
from app.models.task import Task


def save(task):
    db.session.add(task)


def save_ai_job(job):
    db.session.add(job)


def count_active_by_user_id(user_id):
    return Task.query.filter_by(user_id=user_id, status="ACTIVE").count()
