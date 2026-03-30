from sqlalchemy import Column, String, Float, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime
import uuid


class Task(Base):
    __tablename__ = "tasks"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id = Column(String, ForeignKey("students.id"))
    course_id = Column(String, ForeignKey("courses.id"))
    title = Column(String, nullable=False)
    deadline = Column(DateTime)
    weight_percent = Column(Float, default=0.0)
    gpa_impact_score = Column(Float, default=0.0)
    estimated_minutes = Column(Integer, default=60)
    is_completed = Column(Boolean, default=False)
    last_touched_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    student = relationship("Student", back_populates="tasks")
    course = relationship("Course", back_populates="tasks")
    subtasks = relationship("Subtask", back_populates="task")
