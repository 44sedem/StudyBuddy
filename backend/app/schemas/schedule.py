from pydantic import BaseModel
from typing import List

class TimetableEntryCreate(BaseModel):
    course_id: str
    entry_type: str         # CLASS or LAB
    day_of_week: int        # 1–7
    start_time: str
    end_time: str

class FreeSlotResponse(BaseModel):
    start_time: str
    end_time: str
    duration_minutes: int
