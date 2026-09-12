import uuid
from datetime import datetime, timezone
from app.extensions import db


class AIAnalysisHistory(db.Model):
    __tablename__ = "ai_analysis_history"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    task_id = db.Column(db.String(36), db.ForeignKey("task.id", ondelete="CASCADE"), nullable=False, index=True)
    task_version = db.Column(db.Integer, nullable=False)
    idempotency_key = db.Column(db.String(255), nullable=False)
    result_json = db.Column(db.JSON, nullable=False)
    reason_stale = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    __table_args__ = (
        db.Index("ix_ai_history_task_version", "task_id", "task_version"),
    )
