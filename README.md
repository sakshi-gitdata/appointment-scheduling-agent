# 🩺 Appointment Scheduling Agent - Mock Calendly

## Overview
This repository implements a **mock Calendly integration** for a medical appointment scheduling agent using **FastAPI (Python)**.  
It provides endpoints to fetch availability and create bookings (mock).

---

## 🧠 Tech Stack
- **Backend:** FastAPI (Python)  
- **Data:** Mock JSON file (`backend/data/doctor_schedule.json`)  
- **Testing:** cURL scripts in `tests/`

---

## 📁 Folder Structure
Key files and folders:
- `backend/main.py` – FastAPI entry point  
- `backend/api/calendly_integration.py` – availability & booking endpoints  
- `backend/data/doctor_schedule.json` – mock schedule and appointments  
- `backend/models/schemas.py` – Pydantic models  
- `tests/test_endpoints.sh` – example test script  

---

## ⚙️ Setup (Local)

### 1️⃣ Create a virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate   # (For Windows)
# OR on macOS / Linux:
# source venv/bin/activate
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the server
```bash
uvicorn backend.main:app --reload --port 8000
```

### 4️⃣ Open interactive docs
Open your browser and visit:  
http://127.0.0.1:8000/docs

### 5️⃣ Run test script
```bash
./tests/test_endpoints.sh
```

---

## 🧪 API Endpoints

### 🔹 POST `/api/calendly/availability`
**Request Body:**
```json
{
  "date": "YYYY-MM-DD",
  "appointment_type": "consultation"
}
```
**Response:**  
Available time slots in JSON format.

---

### 🔹 POST `/api/calendly/book`
**Request Body:**
```json
{
  "appointment_type": "Consultation",
  "date": "2025-11-10",
  "start_time": "2025-11-10T10:00:00",
  "patient": {
    "name": "Sakshi Sharma",
    "email": "sakshi@example.com",
    "phone": "+919876543210"
  }
}
```
**Response:**  
Booking confirmation with booking ID, status and confirmation code.

---

## 🏗️ Architecture
- The backend handles endpoints and reads/writes from `doctor_schedule.json`.  
- A **mocked Calendly API** is implemented for assessment/testing.  
- Can be extended to integrate with a real Calendly or persistent DB.

---

## 🚀 Future Improvements
- Add conflict detection and slot duration computation.  
- Integrate authentication and persistent DB.  
- Add RAG (Retrieval-Augmented Generation) and LLM for conversational scheduling.  
- Build a simple **React frontend** for fullstack demonstration.

---
