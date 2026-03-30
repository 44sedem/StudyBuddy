from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

async def get_current_student(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    # Decode JWT, fetch student from DB
    pass

async def get_db():
    # Yield async DB session
    pass
