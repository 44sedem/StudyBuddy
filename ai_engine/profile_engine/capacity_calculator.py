def calculate_available_hours(
    total_committed_hours: float,
    timetable_entries: list,
    date: str
) -> float:
    """
    Subtract class/lab hours on a given day from committed daily hours.
    Returns realistic study hours available.
    """
    from datetime import datetime
    day_of_week = datetime.fromisoformat(date).isoweekday()
    scheduled_minutes = sum(
        _duration_minutes(e["start_time"], e["end_time"])
        for e in timetable_entries
        if e["day_of_week"] == day_of_week
    )
    return max(0, total_committed_hours - (scheduled_minutes / 60))

def _duration_minutes(start: str, end: str) -> int:
    sh, sm = map(int, start.split(":"))
    eh, em = map(int, end.split(":"))
    return (eh * 60 + em) - (sh * 60 + sm)
