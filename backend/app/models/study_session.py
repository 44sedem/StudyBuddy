from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from app.core.database import Base
from datetime import datetime
import uuid


class StudySession(Base):
    __tablename__ = "study_sessions"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id = Column(String, ForeignKey("students.id"))
    task_id = Column(String, ForeignKey("tasks.id"), nullable=True)
    technique = Column(String, nullable=False)
    duration_minutes = Column(Integer, default=0)
    started_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime, nullable=True)
