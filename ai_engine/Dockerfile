FROM python:3.12-slim

WORKDIR /ai_engine
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["celery", "-A", "ai_engine.core.background_jobs.celery_app", "worker", "--loglevel=info"]
