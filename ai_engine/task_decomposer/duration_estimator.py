def estimate_total_minutes(task_title: str, credit_hours: int) -> int:
    """Rough heuristic: heavier course weight = longer task"""
    base = 60
    if any(w in task_title.lower() for w in ["essay", "report", "paper"]):
        base = 180
    elif any(w in task_title.lower() for w in ["exam", "midterm", "final"]):
        base = 240
    elif any(w in task_title.lower() for w in ["quiz", "reading"]):
        base = 45
    return base + (credit_hours * 10)
