DECOMPOSE_PROMPT = """
You are a student productivity assistant. Break the following task into clear, ordered subtasks.

Task: {task_title}
Course context: {course_context}
Total estimated time: {total_minutes} minutes

Return ONLY a JSON array of subtasks. Each item:
- "title": string (clear action verb, e.g. "Find 5 academic sources")
- "estimated_minutes": integer
- "order": integer starting at 1

JSON array:
"""
