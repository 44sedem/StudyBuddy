from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class QuizCreate(BaseModel):
    course_id: str
    title: str
    scheduled_date: datetime
    duration_minutes: int = 30
    weight_percent: float
    topics_covered: Optional[str] = None

class QuizResponse(BaseModel):
    id: str
    course_id: str
    title: str
    scheduled_date: datetime
    weight_percent: float
    gpa_impact_score: float
    is_completed: bool
    score_achieved: Optional[float] = None

    class Config:
        from_attributes = True
