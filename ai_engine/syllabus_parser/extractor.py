from ai_engine.core.llm_client import call_llm
from ai_engine.syllabus_parser.prompts import SYLLABUS_EXTRACTION_PROMPT
import json

async def extract_deadlines(raw_text: str) -> list[dict]:
    """Send syllabus text to LLM → returns structured deadline list"""
    prompt = SYLLABUS_EXTRACTION_PROMPT.format(syllabus_text=raw_text)
    response = await call_llm(prompt)
    return json.loads(response)
