from datetime import datetime, timedelta

def find_idle_tasks(tasks: list[dict], idle_days: int = 3) -> list[dict]:
    """Flag tasks not touched in idle_days with deadline within 7 days"""
    now = datetime.now()
    idle = []
    for task in tasks:
        if task.get("is_completed"):
            continue
        last_touched = task.get("last_touched_at")
        deadline = task.get("deadline")
        if not deadline:
            continue
        dl = datetime.fromisoformat(deadline)
        days_until_deadline = (dl - now).days
        if last_touched:
            lt = datetime.fromisoformat(last_touched)
            days_idle = (now - lt).days
        else:
            days_idle = idle_days  # never touched
        if days_idle >= idle_days and days_until_deadline <= 7:
            idle.append({**task, "days_idle": days_idle, "days_until_deadline": days_until_deadline})
    return idle
