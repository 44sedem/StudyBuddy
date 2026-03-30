from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from app.core.database import Base
from datetime import datetime
import uuid


class AccountabilityPair(Base):
    __tablename__ = "accountability_pairs"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    student_a_id = Column(String, ForeignKey("students.id"))
    student_b_id = Column(String, ForeignKey("students.id"))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
