from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from app.core.database import Base
from datetime import datetime
import uuid


class EnergyCheckIn(Base):
    __tablename__ = "energy_checkins"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id = Column(String, ForeignKey("students.id"))
    rating = Column(Integer, nullable=False)
    date = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
