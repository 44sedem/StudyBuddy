from datetime import datetime

def normalize_deadlines(raw: list[dict]) -> list[dict]:
    """Normalize dates, remove duplicates, sort by date"""
    seen = set()
    cleaned = []
    for item in raw:
        key = (item.get("title", ""), item.get("date", ""))
        if key not in seen:
            seen.add(key)
            cleaned.append(item)
    return sorted(cleaned, key=lambda x: x.get("date", ""))
