from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
import uuid


class Course(Base):
    __tablename__ = "courses"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id = Column(String, ForeignKey("students.id"))
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    credit_hours = Column(Integer, nullable=False)
    professor = Column(String)
    color_hex = Column(String, default="#1A73E8")
    student = relationship("Student", back_populates="courses")
    tasks = relationship("Task", back_populates="course")
    quizzes = relationship("Quiz", back_populates="course")
    outlines = relationship("CourseOutline", back_populates="course")
