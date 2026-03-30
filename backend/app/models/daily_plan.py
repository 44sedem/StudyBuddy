from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from app.core.database import Base
from datetime import datetime
import uuid


class DailyPlan(Base):
    __tablename__ = "daily_plans"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id = Column(String, ForeignKey("students.id"))
    date = Column(String, nullable=False)
    energy_rating = Column(Integer)
    planned_tasks_json = Column(String)
    suggested_technique = Column(String)
    generated_at = Column(DateTime, default=datetime.utcnow)
