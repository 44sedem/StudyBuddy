class NotificationService:
    async def send_procrastination_nudge(self, student_id: str, task_title: str, days_idle: int):
        message = f"You haven't started '{task_title}' in {days_idle} days — want me to break it into steps?"
        # Push via FCM / APNs
        pass

    async def send_streak_message(self, student_id: str, streak_days: int):
        pass
