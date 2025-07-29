import os

import pyrebase

# Firebase configuration sourced from environment variables for security
firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY", ""),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN", ""),
    "projectId": os.getenv("FIREBASE_PROJECT_ID", ""),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET", ""),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID", ""),
    "appId": os.getenv("FIREBASE_APP_ID", ""),
    "databaseURL": "",  # Optional for this use-case
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def sign_in(email: str, password: str):
    """Authenticate existing users and return auth payload containing the ID token."""
    return auth.sign_in_with_email_and_password(email, password)


def sign_up(email: str, password: str):
    """Register a new user and return auth payload."""
    return auth.create_user_with_email_and_password(email, password)