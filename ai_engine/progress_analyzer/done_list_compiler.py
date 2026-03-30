from datetime import datetime, timedelta

def compile_weekly_done_list(tasks: list[dict]) -> list[dict]:
    """Returns tasks completed in the past 7 days"""
    cutoff = datetime.now() - timedelta(days=7)
    return [t for t in tasks if t.get("is_completed") and t.get("completed_at") and
            datetime.fromisoformat(t["completed_at"]) >= cutoff]
