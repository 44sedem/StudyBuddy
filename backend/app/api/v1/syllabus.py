from fastapi import APIRouter, UploadFile, File, Depends
from app.core.dependencies import get_current_student

router = APIRouter()

@router.post("/upload/{course_id}")
async def upload_syllabus(
    course_id: str,
    file: UploadFile = File(...),
    student=Depends(get_current_student)
):
    """Upload syllabus PDF → triggers AI parsing pipeline"""
    pass

@router.get("/{course_id}/deadlines")
async def get_extracted_deadlines(course_id: str, student=Depends(get_current_student)):
    """Return AI-extracted deadlines for a course"""
    pass
