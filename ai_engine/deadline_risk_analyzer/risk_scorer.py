def score_week_risk(tasks_in_week: list[dict]) -> float:
    """
    Score = sum of (gpa_impact_score) for all tasks in week.
    Higher score = more critical week.
    """
    return sum(t.get("gpa_impact_score", 0) for t in tasks_in_week)
