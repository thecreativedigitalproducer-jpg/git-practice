from app.extensions import db
from app.models.task import Task
from app.models.ai_job import AIJob
from app.repositories.task_repository import save, save_ai_job
from app.repositories.user_repository import get_by_id

class UserNotFound(Exception):
    pass

def create_task_with_ai(user_id, title, description=None):
    title = (title or "").strip()
    if not title:
        raise ValueError("Title is required.")

    user = get_by_id(user_id)
    if not user:
        raise UserNotFound("User not found.")

    task = Task(user_id=user_id, title=title, description=description)

    try:
        save(task)
        db.session.flush()

        job = AIJob(
            task_id=task.id,
            task_version_analyzed=task.version,
            idempotency_key=f"{task.id}:{task.version}",
        )
        save_ai_job(job)

        db.session.commit()
    except Exception:
        db.session.rollback()
        raise

    return task, job
