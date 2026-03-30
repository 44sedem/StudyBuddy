from sqlalchemy import Column, String, Boolean, ForeignKey
from app.core.database import Base
import uuid


class Reward(Base):
    __tablename__ = "rewards"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id = Column(String, ForeignKey("students.id"))
    title = Column(String, nullable=False)
    trigger_task_id = Column(String, ForeignKey("tasks.id"), nullable=True)
    is_unlocked = Column(Boolean, default=False)
