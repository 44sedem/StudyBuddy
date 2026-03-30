from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:1234@localhost:5432/studybuddy"
    REDIS_URL: str = "redis://localhost:6379"
    SECRET_KEY: str = "change-me-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30
    OPENAI_API_KEY: str = ""
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/1"

    model_config = {"env_file": ".env", "extra": "ignore"}

settings = Settings()