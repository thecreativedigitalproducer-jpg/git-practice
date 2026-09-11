from sqlalchemy.exc import IntegrityError
from app.extensions import db
from app.repositories.user_repository import get_all_users as repository_get_all_users, save
from app.models.user import User


def get_all_users():
    return repository_get_all_users()


def create_user(name, email):
    name = name.strip()
    email = email.strip()

    if not name:
        raise ValueError("Name is required.")

    if not email:
        raise ValueError("Email is required.")

    user = User(name=name, email=email)
    save(user)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise ValueError("Email already exists.")

    return user
