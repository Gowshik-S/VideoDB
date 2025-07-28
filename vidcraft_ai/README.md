# VidCraftAI Quickstart

## Prerequisites
- Python 3.10+
- Firebase project (service account JSON)
- VideoDB API key

## Setup
1. Clone this repository.
2. Install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Set environment variables or update `config.py`:
   - `VIDEODB_API_KEY`
   - `FIREBASE_CREDENTIALS_JSON`
4. Start backend:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
5. Start frontend:
   ```bash
   streamlit run frontend/streamlit_app.py --server.port 8501
   ```

## Integrations
- **VideoDB API**: Update `VIDEODB_API_KEY` in `config.py` or set env var.
- **Firebase**: Place your `serviceAccountKey.json` and set path in env var `FIREBASE_CREDENTIALS_JSON`.
