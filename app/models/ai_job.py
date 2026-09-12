import uuid
from datetime import datetime, timezone
from app.extensions import db


class AIJob(db.Model):
    __tablename__ = "ai_job"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    task_id = db.Column(db.String(36), db.ForeignKey("task.id", ondelete="CASCADE"), nullable=False, index=True)
    task_version_analyzed = db.Column(db.Integer, nullable=False)
    idempotency_key = db.Column(db.String(255), nullable=False, unique=True)
    status = db.Column(db.String(30), nullable=False, default="REQUESTED")
    attempt = db.Column(db.Integer, nullable=False, default=0)
    error_message = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    __table_args__ = (
        db.Index("ix_ai_job_status_created", "status", "created_at"),
        db.Index("ix_ai_job_task_status", "task_id", "status"),
    )
