from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime
import uuid


class CourseOutline(Base):
    __tablename__ = "course_outlines"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    course_id = Column(String, ForeignKey("courses.id"))
    filename = Column(String)
    raw_text = Column(String)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    course = relationship("Course", back_populates="outlines")
