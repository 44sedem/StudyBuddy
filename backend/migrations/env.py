from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.core.database import Base
from app.models.student import Student
from app.models.student_profile import StudentProfile
from app.models.course import Course
from app.models.task import Task
from app.models.subtask import Subtask
from app.models.timetable_entry import TimetableEntry
from app.models.sleep_schedule import SleepSchedule
from app.models.energy_checkin import EnergyCheckIn
from app.models.study_session import StudySession
from app.models.daily_plan import DailyPlan
from app.models.study_plan import StudyPlan
from app.models.reward import Reward
from app.models.accountability_pair import AccountabilityPair
from app.models.group_project import GroupProject
from app.models.quiz import Quiz
from app.models.interim_assessment import InterimAssessment
from app.models.course_outline import CourseOutline
from app.models.weekly_load import WeeklyLoad
from app.models.burnout_score import BurnoutScore

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata


def run_migrations_offline():
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = config.get_main_option("sqlalchemy.url").replace(
        "postgresql+asyncpg", "postgresql+psycopg2"
    )
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
