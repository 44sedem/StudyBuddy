from sqlalchemy import Column, String, Float, Integer, DateTime, Boolean, ForeignKey
from app.core.database import Base
from datetime import datetime
from enum import Enum
import uuid


class AssessmentType(str, Enum):
    MIDTERM = "midterm"
    FINAL = "final"
    INTERIM = "interim"
    PROJECT = "project"
    PRACTICAL = "practical"


class InterimAssessment(Base):
    __tablename__ = "interim_assessments"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id = Column(String, ForeignKey("students.id"))
    course_id = Column(String, ForeignKey("courses.id"))
    title = Column(String, nullable=False)
    assessment_type = Column(String, default=AssessmentType.INTERIM)
    scheduled_date = Column(DateTime)
    duration_minutes = Column(Integer, default=120)
    weight_percent = Column(Float, default=0.0)
    gpa_impact_score = Column(Float, default=0.0)
    topics_covered = Column(String, nullable=True)
    venue = Column(String, nullable=True)
    recommended_prep_days = Column(Integer, default=14)
    is_completed = Column(Boolean, default=False)
    score_achieved = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
