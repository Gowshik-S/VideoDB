
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import firebase_admin
from firebase_admin import credentials, auth
import os
from ... import config

security = HTTPBearer()

def init_firebase():
    if not firebase_admin._apps:
        cred_path = os.getenv('FIREBASE_CREDENTIALS_JSON', config.FIREBASE_CREDENTIALS_JSON)
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)

def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security)):
    try:
        decoded = auth.verify_id_token(credentials.credentials)
        return decoded
    except Exception as exc:
        raise HTTPException(status_code=401, detail='Invalid or expired token') from exc
