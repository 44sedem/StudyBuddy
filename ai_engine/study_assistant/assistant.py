from ai_engine.core.llm_client import call_llm
from ai_engine.study_assistant.context_builder import build_session_context

async def answer_question(question: str, task_title: str, course_name: str, course_code: str) -> str:
    system_context = build_session_context(task_title, course_name, course_code)
    prompt = f"{system_context}\n\nStudent question: {question}\n\nAnswer:"
    return await call_llm(prompt)
