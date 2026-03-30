from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    course_id: str
    deadline: datetime
    weight_percent: float
    estimated_minutes: int = 60

class TaskResponse(BaseModel):
    id: str
    title: str
    gpa_impact_score: float
    is_completed: bool

    class Config:
        from_attributes = True
