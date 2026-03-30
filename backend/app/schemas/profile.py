from pydantic import BaseModel

class ProfileUpdate(BaseModel):
    attention_span_minutes: int
    daily_hours_committed: float
    sleep_bedtime: str
    sleep_wake_time: str
