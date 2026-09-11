from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.services.user_service import get_all_users, create_user, EmailAlreadyExists

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

        try:
            create_user(name, email)
            return redirect(url_for("users.user_home"))
        except ValueError as error:
            return render_template("user_form.html", error=error)

    return render_template("user_form.html")


@users.route("/api/users", methods=["POST"])
def api_create_user():
    data = request.get_json()
    name = data.get("name") if data else None
    email = data.get("email") if data else None

    try:
        user = create_user(name, email)
    except EmailAlreadyExists as error:
        return jsonify({"error": "EMAIL_ALREADY_EXISTS", "message": str(error), "field": "email"}), 409
    except ValueError as error:
        return jsonify({"error": "VALIDATION_ERROR", "message": str(error)}), 400

    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201
