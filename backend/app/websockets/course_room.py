from fastapi import WebSocket
from typing import Dict, List

class CourseRoomManager:
    def __init__(self):
        self.rooms: Dict[str, List[WebSocket]] = {}

    async def connect(self, course_id: str, ws: WebSocket):
        await ws.accept()
        self.rooms.setdefault(course_id, []).append(ws)

    async def broadcast(self, course_id: str, message: str):
        for ws in self.rooms.get(course_id, []):
            await ws.send_text(message)
