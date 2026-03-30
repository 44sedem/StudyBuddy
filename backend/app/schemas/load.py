from pydantic import BaseModel
from typing import List

class WeeklyLoadResponse(BaseModel):
    week_start_date: str
    week_end_date: str
    task_count: int
    quiz_count: int
    assessment_count: int
    total_gpa_weight: float
    load_score: float           # 0.0 → 1.0
    is_high_pressure: bool
    estimated_hours_required: float
    available_hours: float

class SemesterOverviewResponse(BaseModel):
    weeks: List[WeeklyLoadResponse]
    highest_pressure_week: str
    total_weeks_remaining: int
