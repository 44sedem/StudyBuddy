from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class StudentResponse(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
