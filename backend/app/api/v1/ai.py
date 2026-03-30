from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_student

router = APIRouter()

@router.post("/daily-plan")
async def generate_daily_plan(energy_rating: int, student=Depends(get_current_student)):
    """Generate AI daily plan based on energy + schedule + deadlines"""
    pass

@router.post("/decompose-task/{task_id}")
async def decompose_task(task_id: str, student=Depends(get_current_student)):
    """AI breaks task into ordered subtasks with time estimates"""
    pass

@router.get("/collision-weeks")
async def get_collision_weeks(student=Depends(get_current_student)):
    """Return deadline collision risk weeks"""
    pass

@router.post("/study-technique")
async def suggest_technique(energy_rating: int, student=Depends(get_current_student)):
    """Recommend Pomodoro / DeepWork / FiveMin based on profile + energy"""
    pass

@router.post("/chat")
async def study_assistant_chat(message: str, task_id: str = None, student=Depends(get_current_student)):
    """In-session AI study assistant"""
    pass
