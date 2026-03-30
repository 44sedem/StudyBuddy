from celery import shared_task

@shared_task
def run_procrastination_scan():
    """
    Celery background task — runs daily for all active students.
    Finds idle tasks, composes nudges, dispatches notifications.
    """
    pass
