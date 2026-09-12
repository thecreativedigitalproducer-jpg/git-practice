from app.extensions import db
from app.models.user import User

def get_all_users():
    return User.query.all()

def save(user):
    db.session.add(user)


def get_by_id(user_id):
    return User.query.get(user_id)
