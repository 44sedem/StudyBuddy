from collections import defaultdict

def detect_peak_study_hours(sessions: list[dict]) -> list[str]:
    """
    Analyzes past study sessions to find hours with highest completion rates.
    Returns top 3 hours in "HH:00" format.
    """
    hour_scores = defaultdict(float)
    for session in sessions:
        if session.get("started_at") and session.get("duration_minutes", 0) > 0:
            hour = session["started_at"][11:13]
            hour_scores[hour] += session["duration_minutes"]
    top = sorted(hour_scores, key=hour_scores.get, reverse=True)[:3]
    return [f"{h}:00" for h in top]
