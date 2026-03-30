"""
ATLAS message composer.
All student-facing messages from ATLAS are generated here
to ensure consistent voice and tone.
"""
from ai_engine.core.llm_client import call_llm
from ai_engine.atlas.identity import SYSTEM_PROMPT

async def compose_message(situation: str, context: dict) -> str:
    """
    Generate a natural ATLAS message for a given situation.
    Situations: daily_greeting, high_pressure_warning, procrastination_nudge,
                streak_celebration, plan_restructure, burnout_alert, study_tip
    """
    prompt = f"""
{SYSTEM_PROMPT}

Situation: {situation}
Student context: {context}

Write a short ATLAS message (2-3 sentences max) for this situation.
Be specific — reference actual course names, deadlines, or stats from the context.
"""
    return await call_llm(prompt)

async def daily_greeting(student_name: str, energy_rating: int, plan_summary: dict) -> str:
    context = {
        "name": student_name,
        "energy": energy_rating,
        "tasks_today": plan_summary.get("task_count", 0),
        "hardest_deadline": plan_summary.get("nearest_deadline", "none today"),
    }
    return await compose_message("daily_greeting", context)

async def high_pressure_warning(student_name: str, week_label: str, load_details: dict) -> str:
    context = {
        "name": student_name,
        "week": week_label,
        "quizzes": load_details.get("quiz_count", 0),
        "assessments": load_details.get("assessment_count", 0),
        "assignments": load_details.get("task_count", 0),
        "gpa_weight": load_details.get("total_gpa_weight", 0),
    }
    return await compose_message("high_pressure_warning", context)

async def burnout_alert(student_name: str, burnout_score: float, consecutive_days: int) -> str:
    context = {
        "name": student_name,
        "risk_level": "critical" if burnout_score > 0.8 else "high",
        "consecutive_high_days": consecutive_days,
    }
    return await compose_message("burnout_alert", context)

async def plan_restructure_notice(student_name: str, reason: str, changes: list) -> str:
    context = {
        "name": student_name,
        "reason": reason,
        "changes_made": changes,
    }
    return await compose_message("plan_restructure", context)
