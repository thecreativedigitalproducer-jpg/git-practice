from flask import Blueprint, render_template, request, redirect, url_for
from app.services.user_service import get_all_users, create_user

users = Blueprint("users", __name__)

@users.route("/users")
def user_home():
    users = get_all_users()
    return render_template("users.html", users=users)

@users.route("/users/new", methods=["GET", "POST"])
def new_user():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        create_user(name, email)
        return redirect(url_for("users.user_home"))

    return render_template("user_form.html")
