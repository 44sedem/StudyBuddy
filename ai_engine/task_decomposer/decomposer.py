from ai_engine.core.llm_client import call_llm
from ai_engine.task_decomposer.prompts import DECOMPOSE_PROMPT
from ai_engine.task_decomposer.duration_estimator import estimate_total_minutes
import json

async def decompose_task(task_title: str, course_context: str, credit_hours: int) -> list[dict]:
    total = estimate_total_minutes(task_title, credit_hours)
    prompt = DECOMPOSE_PROMPT.format(
        task_title=task_title,
        course_context=course_context,
        total_minutes=total
    )
    response = await call_llm(prompt)
    return json.loads(response)
