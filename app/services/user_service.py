from app.extensions import db
from app.models.user import User

def get_all_users():
    return User.query.all()

def create_user(name, email):
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return user
