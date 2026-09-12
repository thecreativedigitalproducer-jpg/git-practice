import uuid
from datetime import datetime, timezone
from app.extensions import db


class Task(db.Model):
    __tablename__ = "task"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False, index=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    version = db.Column(db.Integer, nullable=False, default=1)
    ai_status = db.Column(db.String(20), nullable=False, default="NONE")
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    __table_args__ = (
        db.Index("ix_task_user_updated", "user_id", "updated_at"),
    )
