from celery import Celery
import os

celery_app = Celery(
    "studybuddy_ai",
    broker=os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/1"),
)

celery_app.conf.beat_schedule = {
    "procrastination-scan-daily": {
        "task": "ai_engine.procrastination_detector.scheduler.run_procrastination_scan",
        "schedule": 86400,  # every 24 hours
    },
}
