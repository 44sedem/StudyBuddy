from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_student

router = APIRouter()

@router.get("/")
async def get_all_study_plans(student=Depends(get_current_student)):
    """Get all active study plans for the student"""
    pass

@router.get("/course/{course_id}")
async def get_study_plan_for_course(course_id: str, student=Depends(get_current_student)):
    pass

@router.post("/generate")
async def generate_study_plan(
    course_id: str,
    target_type: str,
    target_id: str = None,
    student=Depends(get_current_student)
):
    """
    Manually trigger study plan generation.
    ATLAS will auto-generate these later — this is the Stage 1 manual trigger.
    """
    pass

@router.patch("/{plan_id}/restructure")
async def restructure_plan(plan_id: str, reason: str, student=Depends(get_current_student)):
    """Manually restructure a plan — ATLAS will automate this in Stage 2"""
    pass

@router.delete("/{plan_id}")
async def delete_study_plan(plan_id: str, student=Depends(get_current_student)):
    pass
