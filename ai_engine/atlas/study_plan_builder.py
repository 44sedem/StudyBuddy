"""
ATLAS study plan builder.
Creates course-specific study plans for quizzes, assessments, and exams.
Uses course outline topics to sequence learning optimally.
"""
from ai_engine.core.llm_client import call_llm
import json

STUDY_PLAN_PROMPT = """
You are ATLAS, an academic planning AI. Create an optimal study plan for a student.

Student profile:
- Attention span: {attention_span} minutes
- Daily hours available: {daily_hours}
- Preferred technique: {technique}

Course: {course_name} ({credit_hours} credit hours)
Target: {target_type} — "{target_title}"
Date of target: {target_date}
Days available to prepare: {days_available}
Topics to cover (in order): {topics}

Return ONLY a JSON array of study sessions:
[
  {{
    "day": "YYYY-MM-DD",
    "topic": "string",
    "duration_minutes": integer,
    "technique": "POMODORO|DEEP_WORK|FIVE_MINUTE",
    "session_goal": "string (what to achieve this session)"
  }}
]

Space topics across available days. Put harder topics earlier.
Leave the final 2 days for review only. Never exceed daily_hours per day.
"""

async def build_plan(
    student_profile: dict,
    course: dict,
    target: dict,
    topics: list[str],
    days_available: int
) -> list[dict]:
    prompt = STUDY_PLAN_PROMPT.format(
        attention_span=student_profile["attention_span_minutes"],
        daily_hours=student_profile["daily_hours_committed"],
        technique="Pomodoro" if student_profile["attention_span_minutes"] <= 45 else "Deep Work",
        course_name=course["name"],
        credit_hours=course["credit_hours"],
        target_type=target["type"],
        target_title=target["title"],
        target_date=target["date"],
        days_available=days_available,
        topics=", ".join(topics)
    )
    response = await call_llm(prompt, max_tokens=2000)
    return json.loads(response)
