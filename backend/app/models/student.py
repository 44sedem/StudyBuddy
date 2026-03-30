from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime
import uuid


class Student(Base):
    __tablename__ = "students"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    profile = relationship("StudentProfile", back_populates="student", uselist=False)
    courses = relationship("Course", back_populates="student")
    tasks = relationship("Task", back_populates="student")
