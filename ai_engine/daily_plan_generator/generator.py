from ai_engine.daily_plan_generator.energy_adjuster import adjust_for_energy
from ai_engine.daily_plan_generator.slot_fitter import fit_tasks_to_slots
from ai_engine.study_technique_recommender.recommender import get_recommendation

async def generate_daily_plan(context, tasks: list[dict], energy_rating: int) -> dict:
    adjusted = adjust_for_energy(tasks, energy_rating)
    plan = fit_tasks_to_slots(adjusted, context.free_slots)
    technique = get_recommendation(context, energy_rating)
    return {
        "date": context.free_slots[0]["date"] if context.free_slots else None,
        "energy_rating": energy_rating,
        "planned_tasks": plan,
        "suggested_technique": technique,
    }
