from ai_engine.core.llm_client import call_llm

async def compose_nudge(task_title: str, days_idle: int, days_until_deadline: int) -> str:
    prompt = f"""
Write a short, friendly nudge message (max 2 sentences) for a student who hasn't started "{task_title}".
They've had it for {days_idle} days and it's due in {days_until_deadline} days.
Offer to break it into steps. Be warm, not guilt-trippy.
"""
    return await call_llm(prompt)
