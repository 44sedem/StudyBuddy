from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_student
from app.schemas.quiz import QuizCreate, QuizResponse
from typing import List

router = APIRouter()

@router.get("/", response_model=List[QuizResponse])
async def get_all_quizzes(student=Depends(get_current_student)):
    """Get all quizzes for the current student, sorted by date"""
    pass

@router.get("/upcoming")
async def get_upcoming_quizzes(days: int = 14, student=Depends(get_current_student)):
    """Get quizzes scheduled within the next N days"""
    pass

@router.get("/course/{course_id}", response_model=List[QuizResponse])
async def get_quizzes_by_course(course_id: str, student=Depends(get_current_student)):
    pass

@router.post("/", response_model=QuizResponse)
async def create_quiz(data: QuizCreate, student=Depends(get_current_student)):
    pass

@router.patch("/{quiz_id}/complete")
async def mark_quiz_complete(quiz_id: str, score: float, student=Depends(get_current_student)):
    """Mark quiz as done and record the score achieved"""
    pass

@router.delete("/{quiz_id}")
async def delete_quiz(quiz_id: str, student=Depends(get_current_student)):
    pass
