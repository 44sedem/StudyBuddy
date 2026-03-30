from fastapi import HTTPException, status

class StudentNotFound(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

class Unauthorized(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
