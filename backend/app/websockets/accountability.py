from fastapi import WebSocket
from typing import Dict

class AccountabilityManager:
    def __init__(self):
        self.pairs: Dict[str, WebSocket] = {}

    async def notify_pair(self, pair_id: str, event: str):
        ws = self.pairs.get(pair_id)
        if ws:
            await ws.send_text(event)
