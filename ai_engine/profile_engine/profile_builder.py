from dataclasses import dataclass

@dataclass
class AIStudentContext:
    student_id: str
    attention_span_minutes: int
    daily_hours_available: float
    peak_hours: list[str]       # e.g. ["09:00", "13:00"]
    chronotype: str
    free_slots: list[dict]      # [{start, end, duration_minutes}]
    energy_trend: list[int]     # last 7 days ratings

async def build_context(student_id: str, db) -> AIStudentContext:
    """Assembles full AI context object from DB profile + schedule"""
    pass
