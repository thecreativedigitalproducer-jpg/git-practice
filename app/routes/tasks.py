from flask import Blueprint, jsonify, request
from app.services.task_service import create_task_with_ai, UserNotFound

tasks = Blueprint("tasks", __name__)


@tasks.route("/api/tasks", methods=["POST"])
def api_create_task():
    data = request.get_json()
    user_id = data.get("user_id") if data else None  # TODO: Replace with authenticated user_id from JWT in v2.
    title = data.get("title") if data else None
    description = data.get("description") if data else None

    try:
        task, job = create_task_with_ai(user_id, title, description)
    except UserNotFound as error:
        return jsonify({"error": "USER_NOT_FOUND", "message": str(error)}), 404
    except ValueError as error:
        return jsonify({"error": "VALIDATION_ERROR", "message": str(error)}), 400

    return jsonify({
        "id": task.id,
        "user_id": task.user_id,
        "title": task.title,
        "description": task.description,
        "version": task.version,
        "ai_status": task.ai_status,
        "job_id": job.id,
    }), 201
