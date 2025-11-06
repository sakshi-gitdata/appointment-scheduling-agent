# Appointment Scheduling Agent - Mock Calendly

## Overview
This repo implements a mock Calendly integration for a medical appointment scheduling agent using FastAPI (Python). It provides endpoints to fetch availability and create bookings (mock).

## Tech Stack
- Backend: FastAPI (Python)
- Data: Mock JSON file (`backend/data/doctor_schedule.json`)
- Testing: curl scripts in `tests/`

## Folder structure
See the repository's root for structure. Key files:
- `backend/main.py` - FastAPI app
- `backend/api/calendly_integration.py` - availability & booking endpoints
- `backend/data/doctor_schedule.json` - mock schedule and appointments
- `backend/models/schemas.py` - Pydantic models
- `tests/test_endpoints.sh` - example curl tests

## Setup (local)
1. Create virtual environment (recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\\Scripts\\activate
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the server:
   ```
   uvicorn backend.main:app --reload --port 8000
   ```
4. Test endpoints:
   - Open browser: http://127.0.0.1:8000/docs  (interactive docs)
   - Run tests:
     ```
     ./tests/test_endpoints.sh
     ```

## API Endpoints
- `POST /api/calendly/availability`  
  Body: `{ "date": "YYYY-MM-DD", "appointment_type": "consultation" }`  
  Returns available slots.

- `POST /api/calendly/book`  
  Body: booking JSON (see `backend/models/schemas.py`)  
  Returns booking confirmation.

## Architecture
- Backend handles endpoints and reads/writes `doctor_schedule.json`.
- For the assessment, a mocked Calendly API is implemented. Replace with real Calendly endpoints if needed.

## Notes & Future Work
- Improve conflict detection and compute end_time based on slot duration.
- Add authentication, persistent DB, vector DB for RAG, and LLM integration for conversation.
- Add frontend chat interface (React) for fullstack submission.
