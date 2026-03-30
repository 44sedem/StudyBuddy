def detect_chronotype(wake_time: str, bedtime: str) -> str:
    """
    Infer chronotype from sleep schedule.
    Wake before 07:00 → MORNING
    Sleep after 01:00 → EVENING
    Otherwise         → NEUTRAL
    """
    wake_h = int(wake_time.split(":")[0])
    bed_h = int(bedtime.split(":")[0])

    if wake_h <= 6:
        return "MORNING"
    elif bed_h >= 1 or bed_h == 0:
        return "EVENING"
    return "NEUTRAL"

def get_peak_hours(chronotype: str) -> list[str]:
    peaks = {
        "MORNING": ["07:00", "08:00", "09:00", "10:00"],
        "EVENING": ["15:00", "16:00", "20:00", "21:00"],
        "NEUTRAL": ["09:00", "10:00", "14:00", "15:00"]
    }
    return peaks.get(chronotype, peaks["NEUTRAL"])
