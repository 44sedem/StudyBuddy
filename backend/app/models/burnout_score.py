from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from app.core.database import Base
from datetime import datetime
import uuid


class BurnoutScore(Base):
    __tablename__ = "burnout_scores"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id = Column(String, ForeignKey("students.id"))
    score = Column(Float, default=0.0)
    computed_at = Column(DateTime, default=datetime.utcnow)
