from sqlalchemy import Column, String, DateTime, ForeignKey
from app.core.database import Base
from datetime import datetime
import uuid


class StudyPlan(Base):
    __tablename__ = "study_plans"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id = Column(String, ForeignKey("students.id"))
    course_id = Column(String, ForeignKey("courses.id"))
    content_json = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
