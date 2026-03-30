SYLLABUS_EXTRACTION_PROMPT = """
You are an academic assistant. Extract all deadlines, assignments, quizzes, exams, and submission dates from the syllabus below.

Return ONLY a valid JSON array. Each item must have:
- "title": string (e.g. "Midterm Exam", "Assignment 1")
- "date": string in ISO format "YYYY-MM-DD"
- "type": one of ["assignment", "exam", "quiz", "project", "lab", "other"]
- "weight_percent": number or null if not mentioned

Syllabus:
{syllabus_text}

JSON array:
"""
