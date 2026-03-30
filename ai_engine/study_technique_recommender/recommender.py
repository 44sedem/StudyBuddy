from ai_engine.study_technique_recommender.rules import recommend
from ai_engine.profile_engine.profile_builder import AIStudentContext

def get_recommendation(context: AIStudentContext, energy_rating: int) -> dict:
    technique = recommend(context.attention_span_minutes, energy_rating)
    return {
        "technique": technique.name,
        "focus_minutes": technique.focus_minutes,
        "break_minutes": technique.break_minutes,
        "reason": f"Based on your {context.attention_span_minutes}-min attention span and energy level {energy_rating}/5"
    }
