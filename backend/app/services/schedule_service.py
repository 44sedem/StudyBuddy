from datetime import datetime, timedelta

class ScheduleService:
    def __init__(self, repo):
        self.repo = repo

    async def get_free_slots(self, student_id: str, date: str):
        """Returns free time blocks after removing class/lab/sleep time"""
        timetable = await self.repo.get_timetable(student_id)
        sleep = await self.repo.get_sleep_schedule(student_id)
        # Compute gaps between scheduled blocks
        return []  # TODO: implement slot detection

    async def detect_peak_hours(self, student_id: str):
        """Infer chronotype peak from sleep schedule"""
        pass
