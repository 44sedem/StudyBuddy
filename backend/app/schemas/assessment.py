from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.interim_assessment import AssessmentType

class AssessmentCreate(BaseModel):
    course_id: str
    title: str
    assessment_type: AssessmentType
    scheduled_date: datetime
    duration_minutes: int = 120
    weight_percent: float
    topics_covered: Optional[str] = None
    venue: Optional[str] = None
    recommended_prep_days: int = 14

class AssessmentResponse(BaseModel):
    id: str
    course_id: str
    title: str
    assessment_type: AssessmentType
    scheduled_date: datetime
    weight_percent: float
    gpa_impact_score: float
    is_completed: bool
    score_achieved: Optional[float] = None

    class Config:
        from_attributes = True
