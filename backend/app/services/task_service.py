class TaskService:
    def __init__(self, repo):
        self.repo = repo

    async def compute_gpa_impact(self, weight_percent: float, credit_hours: int) -> float:
        """Higher weight in more credit-heavy course = higher priority"""
        return weight_percent * credit_hours

    async def get_idle_tasks(self, student_id: str, idle_days: int = 3):
        """Detect tasks untouched for idle_days with approaching deadlines"""
        return await self.repo.get_idle_tasks_near_deadline(student_id, idle_days)
