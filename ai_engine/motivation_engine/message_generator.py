from ai_engine.core.llm_client import call_llm

async def generate_encouragement(student_name: str, streak_days: int, subject: str) -> str:
    prompt = f"""
Write a short encouraging message (1–2 sentences) for {student_name}, a student who has been on a {streak_days}-day study streak studying {subject}.
Be genuine and specific. Avoid clichés.
"""
    return await call_llm(prompt)
