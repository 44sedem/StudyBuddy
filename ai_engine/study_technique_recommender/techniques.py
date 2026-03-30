from dataclasses import dataclass

@dataclass
class Technique:
    name: str
    focus_minutes: int
    break_minutes: int
    best_for: str

POMODORO    = Technique("Pomodoro",    25,  5, "Most students, moderate attention span")
DEEP_WORK   = Technique("Deep Work",   90, 20, "Long attention span, complex tasks")
FIVE_MINUTE = Technique("5-Minute Rule", 5,  0, "Low energy, procrastination, getting started")
SHORT_BURST = Technique("Short Burst", 15,  5, "Very short attention span or high fatigue")
