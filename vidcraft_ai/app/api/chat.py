
from fastapi import APIRouter, Depends
from ..auth.firebase_auth import get_current_user
from ..services.videodb_service import db_service

router = APIRouter(prefix='/chat', tags=['chat'])

@router.get('/ping')
async def ping(current_user: dict = Depends(get_current_user)):
    return await db_service.health()
