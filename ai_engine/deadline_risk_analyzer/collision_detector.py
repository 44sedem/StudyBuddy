from collections import defaultdict
from datetime import datetime, timedelta

def detect_collision_weeks(tasks: list[dict], threshold: int = 3) -> list[str]:
    """Returns list of week labels where deadline count >= threshold"""
    week_counts = defaultdict(int)
    for task in tasks:
        if task.get("deadline"):
            dt = datetime.fromisoformat(task["deadline"])
            week_start = dt - timedelta(days=dt.weekday())
            week_key = week_start.strftime("Week of %b %d")
            week_counts[week_key] += 1
    return [w for w, count in week_counts.items() if count >= threshold]
