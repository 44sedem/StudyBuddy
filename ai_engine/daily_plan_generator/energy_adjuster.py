def adjust_for_energy(tasks: list[dict], energy_rating: int) -> list[dict]:
    """
    Energy 1-2: return only top 3 tasks, lightest first
    Energy 3:   return top 5, balanced order
    Energy 4-5: full list, hardest (highest gpa_impact) first
    """
    if energy_rating <= 2:
        light = sorted(tasks, key=lambda t: t.get("estimated_minutes", 60))
        return light[:3]
    elif energy_rating == 3:
        return tasks[:5]
    else:
        return sorted(tasks, key=lambda t: t.get("gpa_impact_score", 0), reverse=True)
