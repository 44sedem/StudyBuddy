from pydantic import BaseModel
from typing import Optional

class DailyPlanRequest(BaseModel):
    energy_rating: int      # 1–5
    date: str               # "2025-03-26"

class TaskDecomposeRequest(BaseModel):
    task_id: str

class StudyChatRequest(BaseModel):
    message: str
    task_id: Optional[str] = None
    course_context: Optional[str] = None

class TechniqueRequest(BaseModel):
    energy_rating: int
