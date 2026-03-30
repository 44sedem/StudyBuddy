# StudyBuddy — The App That Thinks Like a Student

> A cross-platform productivity app for university students — mobile, desktop, and AI-powered.

## Stack
| Layer | Tech |
|---|---|
| Frontend | Kotlin · Compose Multiplatform (Android, iOS, Desktop) |
| Backend | Python · FastAPI · SQLAlchemy |
| Database | PostgreSQL + Redis |
| AI Engine | Python · Celery · OpenAI API |
| Build | Gradle (Kotlin DSL) · Docker · GitHub Actions |

## Getting Started

### Backend + Database
```bash
docker-compose up -d
cd backend && uvicorn app.main:app --reload
```

### Frontend (Desktop)
```bash
./gradlew :composeApp:run
```

### Android
```bash
./gradlew :composeApp:assembleDebug
```

## Architecture
- `composeApp/` — Compose Multiplatform UI (all platforms from one codebase)
- `shared/` — Kotlin Multiplatform business logic, domain models, use cases
- `backend/` — FastAPI REST API + WebSocket server
- `ai_engine/` — Standalone AI pipeline (syllabus parser, daily planner, procrastination detector, etc.)

## Key Features
- Syllabus PDF parser → auto-populate semester deadlines
- GPA-impact-weighted task prioritization
- Energy-aware daily plan generator (1–5 check-in each morning)
- Study technique recommender (Pomodoro / Deep Work / 5-Minute Rule)
- Deadline collision heatmap
- Procrastination nudge system
- In-session AI study assistant
- Accountability pairs + course rooms
- Weekly Done List + reward unlock system

## Environment
Copy `backend/.env` and fill in your values:
- `DATABASE_URL` — PostgreSQL connection string
- `OPENAI_API_KEY` — LLM provider key
- `SECRET_KEY` — JWT signing secret
