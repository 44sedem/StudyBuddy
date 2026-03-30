from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey
from app.core.database import Base
from datetime import datetime
import uuid


class WeeklyLoad(Base):
    __tablename__ = "weekly_loads"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id = Column(String, ForeignKey("students.id"))
    week_start = Column(String, nullable=False)
    task_count = Column(Integer, default=0)
    total_weight = Column(Float, default=0.0)
    risk_score = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
