from app.extensions import db
from app.models.task import Task


def save(task):
    db.session.add(task)


def save_ai_job(job):
    db.session.add(job)
