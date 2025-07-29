
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin.exceptions import InvalidArgumentError, FirebaseError
import os
import logging
from ... import config

logger = logging.getLogger(__name__)
security = HTTPBearer()

def init_firebase():
    if not firebase_admin._apps:
        cred_path = os.getenv('FIREBASE_CREDENTIALS_JSON', config.FIREBASE_CREDENTIALS_JSON)
        
        # Validate credentials path exists
        if not os.path.exists(cred_path):
            logger.error(f"Firebase credentials file not found: {cred_path}")
            raise FileNotFoundError(f"Firebase credentials file not found: {cred_path}")
            
        try:
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
            logger.info("Firebase initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Firebase: {e}")
            raise

def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security)):
    if not credentials or not credentials.credentials:
        logger.warning("Authentication attempted without credentials")
        raise HTTPException(status_code=401, detail='Authentication required')
    
    try:
        decoded = auth.verify_id_token(credentials.credentials)
        return decoded
    except auth.InvalidIdTokenError:
        logger.warning("Invalid ID token provided")
        raise HTTPException(status_code=401, detail='Invalid authentication token')
    except auth.ExpiredIdTokenError:
        logger.warning("Expired ID token provided")
        raise HTTPException(status_code=401, detail='Authentication token has expired')
    except auth.RevokedIdTokenError:
        logger.warning("Revoked ID token provided")
        raise HTTPException(status_code=401, detail='Authentication token has been revoked')
    except InvalidArgumentError:
        logger.warning("Invalid token format provided")
        raise HTTPException(status_code=401, detail='Invalid authentication token format')
    except FirebaseError as e:
        logger.error(f"Firebase authentication error: {e}")
        raise HTTPException(status_code=500, detail='Authentication service error')
    except Exception as e:
        # Log the actual error for debugging but don't expose it
        logger.error(f"Unexpected authentication error: {e}")
        raise HTTPException(status_code=401, detail='Authentication failed')
