from ai_engine.progress_analyzer.pattern_detector import detect_peak_study_hours

def suggest_best_study_time(sessions: list[dict], task_complexity: str = "medium") -> str:
    peaks = detect_peak_study_hours(sessions)
    if not peaks:
        return "09:00"
    return peaks[0]
