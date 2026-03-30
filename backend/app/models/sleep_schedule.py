from sqlalchemy import Column, String, ForeignKey
from app.core.database import Base
import uuid


class SleepSchedule(Base):
    __tablename__ = "sleep_schedules"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id = Column(String, ForeignKey("students.id"), unique=True)
    bedtime = Column(String, nullable=False)
    wake_time = Column(String, nullable=False)
