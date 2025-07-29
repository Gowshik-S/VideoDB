
import os
import logging
from typing import Dict, Any, Optional
from ... import config

logger = logging.getLogger(__name__)

try:
    from videodb import VideoDB, connect
    VIDEODB_AVAILABLE = True
except ImportError as e:
    logger.warning(f"VideoDB not available: {e}")
    VideoDB = None
    VIDEODB_AVAILABLE = False
    def connect(api_key: str):
        pass

class VideoDBService:
    def __init__(self):
        self.vdb: Optional[VideoDB] = None
        self._initialized = False
        
        if not VIDEODB_AVAILABLE:
            logger.error("VideoDB library is not installed. Install with: pip install videodb")
            return
            
        api_key = os.getenv('VIDEODB_API_KEY', config.VIDEODB_API_KEY)
        
        # Validate API key
        if not api_key or api_key == 'YOUR_VIDEODB_API_KEY':
            logger.error("VideoDB API key not configured. Set VIDEODB_API_KEY environment variable.")
            return
            
        try:
            connect(api_key=api_key)
            if VideoDB:
                self.vdb = VideoDB()
                self._initialized = True
                logger.info("VideoDB service initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize VideoDB: {e}")

    async def health(self) -> Dict[str, Any]:
        if not self._initialized:
            return {
                'status': 'error',
                'message': 'VideoDB service not properly initialized',
                'videodb_available': VIDEODB_AVAILABLE
            }
        return {
            'status': 'ok',
            'videodb_available': VIDEODB_AVAILABLE,
            'initialized': self._initialized
        }

db_service = VideoDBService()
