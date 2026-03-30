from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_student

router = APIRouter()

@router.get("/weekly")
async def get_weekly_loads(weeks: int = 8, student=Depends(get_current_student)):
    """
    Returns load score for each of the next N weeks.
    Used to render the deadline heatmap and pressure calendar.
    """
    pass

@router.get("/burnout-score")
async def get_burnout_score(student=Depends(get_current_student)):
    """Current cumulative burnout risk score 0.0 → 1.0"""
    pass

@router.get("/burnout-history")
async def get_burnout_history(days: int = 30, student=Depends(get_current_student)):
    """Burnout score trend over the past N days"""
    pass

@router.get("/high-pressure-weeks")
async def get_high_pressure_weeks(student=Depends(get_current_student)):
    """Weeks flagged as high pressure by load scoring"""
    pass

@router.get("/semester-overview")
async def get_semester_overview(student=Depends(get_current_student)):
    """
    Full semester load map — every week scored and color-coded.
    Powers the semester-at-a-glance calendar.
    """
    pass
