from ai_engine.study_technique_recommender.techniques import (
    Technique, POMODORO, DEEP_WORK, FIVE_MINUTE, SHORT_BURST
)

def recommend(attention_span_minutes: int, energy_rating: int, task_complexity: str = "medium") -> Technique:
    """
    Rule-based technique selector:
    Energy 1–2                 → FIVE_MINUTE (just get started)
    Attention < 20             → SHORT_BURST
    Attention 20–45, energy 3+ → POMODORO
    Attention 60+, energy 4+   → DEEP_WORK
    """
    if energy_rating <= 2:
        return FIVE_MINUTE
    if attention_span_minutes < 20:
        return SHORT_BURST
    if attention_span_minutes >= 60 and energy_rating >= 4:
        return DEEP_WORK
    return POMODORO
