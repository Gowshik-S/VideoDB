
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import os

from .auth.firebase_auth import init_firebase
from .api import chat as chat_router

init_firebase()

app = FastAPI(title='VidCraftAI API', version='0.1.0')

app.add_middleware(TrustedHostMiddleware, allowed_hosts=['*'])
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv('ALLOWED_ORIGINS', '*').split(','),
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(chat_router.router)

@app.get('/')
async def root():
    return {'message': 'VidCraftAI API running'}
