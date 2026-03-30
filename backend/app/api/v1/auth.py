from fastapi import APIRouter
from app.schemas.student import StudentCreate, TokenResponse

router = APIRouter()

@router.post("/register")
async def register(data: StudentCreate):
    """Register a new student account"""
    pass

@router.post("/login")
async def login():
    """Authenticate and return JWT tokens"""
    pass

@router.post("/refresh")
async def refresh_token():
    """Refresh access token"""
    pass
