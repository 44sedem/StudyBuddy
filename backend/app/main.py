from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import (
    auth, students, profile, courses, syllabus,
    tasks, schedule, energy, sessions, social, ai,
    notifications, progress, quizzes, assessments,
    study_plans, load
)

app = FastAPI(
    title="StudyBuddy API",
    description="Backend API for StudyBuddy — powered by ATLAS",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Auth
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])

# Student
app.include_router(students.router, prefix="/api/v1/students", tags=["Students"])
app.include_router(profile.router, prefix="/api/v1/profile", tags=["Profile"])

# Academic
app.include_router(courses.router, prefix="/api/v1/courses", tags=["Courses"])
app.include_router(syllabus.router, prefix="/api/v1/syllabus", tags=["Syllabus"])
app.include_router(quizzes.router, prefix="/api/v1/quizzes", tags=["Quizzes"])
app.include_router(assessments.router, prefix="/api/v1/assessments", tags=["Assessments"])

# Tasks & Planning
app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["Tasks"])
app.include_router(study_plans.router, prefix="/api/v1/study-plans", tags=["Study Plans"])
app.include_router(schedule.router, prefix="/api/v1/schedule", tags=["Schedule"])

# Load & Burnout
app.include_router(load.router, prefix="/api/v1/load", tags=["Load & Burnout"])

# Daily
app.include_router(energy.router, prefix="/api/v1/energy", tags=["Energy"])
app.include_router(sessions.router, prefix="/api/v1/sessions", tags=["Study Sessions"])

# Social
app.include_router(social.router, prefix="/api/v1/social", tags=["Social"])

# Progress
app.include_router(progress.router, prefix="/api/v1/progress", tags=["Progress"])
app.include_router(notifications.router, prefix="/api/v1/notifications", tags=["Notifications"])

# ATLAS (Stage 2 — endpoints stubbed, not active in Stage 1)
app.include_router(ai.router, prefix="/api/v1/atlas", tags=["ATLAS AI"])
