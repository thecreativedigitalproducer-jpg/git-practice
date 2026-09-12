import uuid
from datetime import datetime, timezone
from app.extensions import db


class AIAnalysisResult(db.Model):
    __tablename__ = "ai_analysis_result"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    task_id = db.Column(db.String(36), db.ForeignKey("task.id", ondelete="CASCADE"), nullable=False, index=True)
    task_version = db.Column(db.Integer, nullable=False)
    idempotency_key = db.Column(db.String(255), nullable=False, unique=True)
    result_json = db.Column(db.JSON, nullable=False)
    tokens_used = db.Column(db.Integer, nullable=True)
    cost_usd = db.Column(db.Numeric(10, 6), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    __table_args__ = (
        db.Index("ix_ai_result_task_version", "task_id", "task_version"),
    )
