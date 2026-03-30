from sqlalchemy import Column, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime
import uuid


class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id = Column(String, ForeignKey("students.id"))
    course_id = Column(String, ForeignKey("courses.id"))
    title = Column(String, nullable=False)
    deadline = Column(DateTime)
    weight_percent = Column(Float, default=0.0)
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    course = relationship("Course", back_populates="quizzes")
