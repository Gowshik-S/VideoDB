
import os
from typing import Dict, Any
from ... import config

try:
    from videodb import VideoDB, connect
except ImportError:
    VideoDB = None
    def connect(api_key: str):
        pass

class VideoDBService:
    def __init__(self):
        api_key = os.getenv('VIDEODB_API_KEY', config.VIDEODB_API_KEY)
        if VideoDB is None:
            # VideoDB library unavailable; operate in stub mode to keep API responsive during development.
            self.vdb = None
        else:
            connect(api_key=api_key)
            self.vdb = VideoDB()

    async def health(self) -> Dict[str, Any]:
        return {'status': 'ok'}

db_service = VideoDBService()
