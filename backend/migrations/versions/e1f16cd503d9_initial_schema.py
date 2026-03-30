"""initial_schema

Revision ID: e1f16cd503d9
Revises:
Create Date: 2025-03-26

"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = "e1f16cd503d9"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "students",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_index("ix_students_email", "students", ["email"])

    op.create_table(
        "student_profiles",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("student_id", sa.String(), nullable=True),
        sa.Column("attention_span_minutes", sa.Integer(), nullable=True),
        sa.Column("daily_hours_committed", sa.Float(), nullable=True),
        sa.Column("sleep_bedtime", sa.String(), nullable=True),
        sa.Column("sleep_wake_time", sa.String(), nullable=True),
        sa.Column("chronotype", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(["student_id"], ["students.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("student_id"),
    )

    op.create_table(
        "sleep_schedules",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("student_id", sa.String(), nullable=True),
        sa.Column("bedtime", sa.String(), nullable=False),
        sa.Column("wake_time", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(["student_id"], ["students.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("student_id"),
    )

    op.create_table(
        "courses",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("student_id", sa.String(), nullable=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("code", sa.String(), nullable=False),
        sa.Column("credit_hours", sa.Integer(), nullable=False),
        sa.Column("professor", sa.String(), nullable=True),
        sa.Column("color_hex", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(["student_id"], ["students.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "timetable_entries",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("student_id", sa.String(), nullable=True),
        sa.Column("course_id", sa.String(), nullable=True),
        sa.Column("entry_type", sa.String(), nullable=False),
        sa.Column("day_of_week", sa.Integer(), nullable=False),
        sa.Column("start_time", sa.String(), nullable=False),
        sa.Column("end_time", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(["student_id"], ["students.id"]),
        sa.ForeignKeyConstraint(["course_id"], ["courses.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "tasks",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("student_id", sa.String(), nullable=True),
        sa.Column("course_id", sa.String(), nullable=True),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("deadline", sa.DateTime(), nullable=True),
        sa.Column("weight_percent", sa.Float(), nullable=True),
        sa.Column("gpa_impact_score", sa.Float(), nullable=True),
        sa.Column("estimated_minutes", sa.Integer(), nullable=True),
        sa.Column("is_completed", sa.Boolean(), nullable=True),
        sa.Column("last_touched_at", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["student_id"], ["students.id"]),
        sa.ForeignKeyConstraint(["course_id"], ["courses.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "subtasks",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("task_id", sa.String(), nullable=True),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("estimated_minutes", sa.Integer(), nullable=True),
        sa.Column("is_completed", sa.Boolean(), nullable=True),
        sa.Column("order", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["task_id"], ["tasks.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "quizzes",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("student_id", sa.String(), nullable=True),
        sa.Column("course_id", sa.String(), nullable=True),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("deadline", sa.DateTime(), nullable=True),
        sa.Column("weight_percent", sa.Float(), nullable=True),
        sa.Column("is_completed", sa.Boolean(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["student_id"], ["students.id"]),
        sa.ForeignKeyConstraint(["course_id"], ["courses.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "interim_assessments",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("student_id", sa.String(), nullable=True),
        sa.Column("course_id", sa.String(), nullable=True),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("assessment_type", sa.String(), nullable=True),
        sa.Column("scheduled_date", sa.DateTime(), nullable=True),
        sa.Column("duration_minutes", sa.Integer(), nullable=True),
        sa.Column("weight_percent", sa.Float(), nullable=True),
        sa.Column("gpa_impact_score", sa.Float(), nullable=True),
        sa.Column("topics_covered", sa.String(), nullable=True),
        sa.Column("venue", sa.String(), nullable=True),
        sa.Column("recommended_prep_days", sa.Integer(), nullable=True),
        sa.Column("is_completed", sa.Boolean(), nullable=True),
        sa.Column("score_achieved", sa.Float(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["student_id"], ["students.id"]),
        sa.ForeignKeyConstraint(["course_id"], ["courses.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "course_outlines",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("course_id", sa.String(), nullable=True),
        sa.Column("filename", sa.String(), nullable=True),
        sa.Column("raw_text", sa.String(), nullable=True),
        sa.Column("uploaded_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["course_id"], ["courses.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "energy_checkins",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("student_id", sa.String(), nullable=True),
        sa.Column("rating", sa.Integer(), nullable=False),
        sa.Column("date", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["student_id"], ["students.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "study_sessions",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("student_id", sa.String(), nullable=True),
        sa.Column("task_id", sa.String(), nullable=True),
        sa.Column("technique", sa.String(), nullable=False),
        sa.Column("duration_minutes", sa.Integer(), nullable=True),
        sa.Column("started_at", sa.DateTime(), nullable=True),
        sa.Column("ended_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["student_id"], ["students.id"]),
        sa.ForeignKeyConstraint(["task_id"], ["tasks.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "daily_plans",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("student_id", sa.String(), nullable=True),
        sa.Column("date", sa.String(), nullable=False),
        sa.Column("energy_rating", sa.Integer(), nullable=True),
        sa.Column("planned_tasks_json", sa.String(), nullable=True),
        sa.Column("suggested_technique", sa.String(), nullable=True),
        sa.Column("generated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["student_id"], ["students.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "study_plans",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("student_id", sa.String(), nullable=True),
        sa.Column("course_id", sa.String(), nullable=True),
        sa.Column("content_json", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["student_id"], ["students.id"]),
        sa.ForeignKeyConstraint(["course_id"], ["courses.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "rewards",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("student_id", sa.String(), nullable=True),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("trigger_task_id", sa.String(), nullable=True),
        sa.Column("is_unlocked", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(["student_id"], ["students.id"]),
        sa.ForeignKeyConstraint(["trigger_task_id"], ["tasks.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "accountability_pairs",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("student_a_id", sa.String(), nullable=True),
        sa.Column("student_b_id", sa.String(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["student_a_id"], ["students.id"]),
        sa.ForeignKeyConstraint(["student_b_id"], ["students.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "group_projects",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("course_id", sa.String(), nullable=True),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["course_id"], ["courses.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "weekly_loads",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("student_id", sa.String(), nullable=True),
        sa.Column("week_start", sa.String(), nullable=False),
        sa.Column("task_count", sa.Integer(), nullable=True),
        sa.Column("total_weight", sa.Float(), nullable=True),
        sa.Column("risk_score", sa.Float(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["student_id"], ["students.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "burnout_scores",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("student_id", sa.String(), nullable=True),
        sa.Column("score", sa.Float(), nullable=True),
        sa.Column("computed_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["student_id"], ["students.id"]),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("burnout_scores")
    op.drop_table("weekly_loads")
    op.drop_table("group_projects")
    op.drop_table("accountability_pairs")
    op.drop_table("rewards")
    op.drop_table("study_plans")
    op.drop_table("daily_plans")
    op.drop_table("study_sessions")
    op.drop_table("energy_checkins")
    op.drop_table("course_outlines")
    op.drop_table("interim_assessments")
    op.drop_table("quizzes")
    op.drop_table("subtasks")
    op.drop_table("tasks")
    op.drop_table("timetable_entries")
    op.drop_table("courses")
    op.drop_table("sleep_schedules")
    op.drop_table("student_profiles")
    op.drop_table("students")
