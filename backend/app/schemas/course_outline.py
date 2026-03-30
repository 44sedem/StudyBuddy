from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CourseOutlineResponse(BaseModel):
    id: str
    course_id: str
    file_name: Optional[str]
    is_parsed: bool
    topics: Optional[str]
    week_by_week_plan: Optional[str]
    uploaded_at: datetime
    parsed_at: Optional[datetime]

    class Config:
        from_attributes = True
