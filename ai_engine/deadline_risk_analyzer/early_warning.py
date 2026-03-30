from datetime import datetime, timedelta

def get_upcoming_risk_weeks(tasks: list[dict], lookahead_weeks: int = 3) -> list[dict]:
    """
    Returns high-risk weeks within the next N weeks.
    """
    now = datetime.now()
    cutoff = now + timedelta(weeks=lookahead_weeks)
    upcoming = [t for t in tasks if t.get("deadline") and now < datetime.fromisoformat(t["deadline"]) <= cutoff]
    return upcoming
