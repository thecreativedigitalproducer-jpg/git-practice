from app.extensions import db
from app.models.user import User

def get_all_users():
    return User.query.all()

def save(user):
    db.session.add(user)
