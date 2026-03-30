from sqlalchemy import Column, String, DateTime, ForeignKey
from app.core.database import Base
from datetime import datetime
import uuid


class GroupProject(Base):
    __tablename__ = "group_projects"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    course_id = Column(String, ForeignKey("courses.id"))
    title = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
