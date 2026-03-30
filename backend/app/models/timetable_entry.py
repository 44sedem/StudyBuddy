from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
import uuid


class TimetableEntry(Base):
    __tablename__ = "timetable_entries"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id = Column(String, ForeignKey("students.id"))
    course_id = Column(String, ForeignKey("courses.id"))
    entry_type = Column(String, nullable=False)
    day_of_week = Column(Integer, nullable=False)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)
