from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
import uuid


class StudentProfile(Base):
    __tablename__ = "student_profiles"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id = Column(String, ForeignKey("students.id"), unique=True)
    attention_span_minutes = Column(Integer, default=25)
    daily_hours_committed = Column(Float, default=4.0)
    sleep_bedtime = Column(String)
    sleep_wake_time = Column(String)
    chronotype = Column(String, default="UNKNOWN")
    student = relationship("Student", back_populates="profile")
