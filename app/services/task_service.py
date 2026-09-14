from app.extensions import db
from app.models.task import Task
from app.models.ai_job import AIJob
from app.repositories.task_repository import save, save_ai_job, count_active_by_user_id
from app.repositories.user_repository import get_by_id

MAX_ACTIVE_TASKS = 10

class UserNotFound(Exception):
    pass


class ActiveTaskLimitExceeded(Exception):
    def __init__(self, user_id, current_count, limit):
        self.user_id = user_id
        self.current_count = current_count
        self.limit = limit
        super().__init__(f"Active task limit exceeded: {current_count}/{limit}.")

def create_task_with_ai(user_id, title, description=None):
    title = (title or "").strip()
    if not title:
        raise ValueError("Title is required.")

    user = get_by_id(user_id)
    if not user:
        raise UserNotFound("User not found.")

    current_count = count_active_by_user_id(user_id)
    if current_count >= MAX_ACTIVE_TASKS:
        raise ActiveTaskLimitExceeded(user_id, current_count, MAX_ACTIVE_TASKS)

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
