def compute_streak(completion_dates: list[str]) -> int:
    """Count consecutive days with at least one task completed"""
    from datetime import datetime, timedelta
    if not completion_dates:
        return 0
    dates = sorted(set(completion_dates), reverse=True)
    streak = 1
    for i in range(1, len(dates)):
        d1 = datetime.fromisoformat(dates[i-1])
        d2 = datetime.fromisoformat(dates[i])
        if (d1 - d2).days == 1:
            streak += 1
        else:
            break
    return streak
