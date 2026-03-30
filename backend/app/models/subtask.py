from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
import uuid


class Subtask(Base):
    __tablename__ = "subtasks"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    task_id = Column(String, ForeignKey("tasks.id"))
    title = Column(String, nullable=False)
    estimated_minutes = Column(Integer, default=30)
    is_completed = Column(Boolean, default=False)
    order = Column(Integer, default=0)
    task = relationship("Task", back_populates="subtasks")
