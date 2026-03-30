def fit_tasks_to_slots(tasks: list[dict], free_slots: list[dict]) -> list[dict]:
    """
    Assign tasks to free time slots in the student's day.
    Returns list of {task_id, start_time, end_time} dicts.
    """
    plan = []
    slot_idx = 0
    for task in tasks:
        if slot_idx >= len(free_slots):
            break
        slot = free_slots[slot_idx]
        plan.append({
            "task_id": task["id"],
            "start_time": slot["start_time"],
            "end_time": slot["end_time"],
        })
        slot_idx += 1
    return plan
