
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import os

from .auth.firebase_auth import init_firebase
from .api import chat as chat_router
from .. import config

init_firebase()

app = FastAPI(title='VidCraftAI API', version='0.1.0')

# Get allowed origins from environment or config, with secure defaults
allowed_origins_env = os.getenv('ALLOWED_ORIGINS')
if allowed_origins_env:
    allowed_origins = allowed_origins_env.split(',')
else:
    allowed_origins = config.ALLOWED_ORIGINS

# Only allow wildcard in development - in production, use specific domains
if '*' in allowed_origins and os.getenv('ENVIRONMENT', 'development') == 'production':
    allowed_origins = ['https://yourdomain.com']  # Replace with actual production domain

app.add_middleware(TrustedHostMiddleware, allowed_hosts=['localhost', '127.0.0.1', 'yourdomain.com'])
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],  # Restrict to needed methods
    allow_headers=['Authorization', 'Content-Type'],  # Restrict to needed headers
)

app.include_router(chat_router.router)

@app.get('/')
async def root():
    return {'message': 'VidCraftAI API running'}
