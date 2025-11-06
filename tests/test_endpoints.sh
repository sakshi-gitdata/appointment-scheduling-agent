#!/bin/bash
# Make sure the server is running (uvicorn backend.main:app --reload --port 8000)

echo "Testing availability for 2025-11-05"
curl -s -X POST "http://127.0.0.1:8000/api/calendly/availability"           -H "Content-Type: application/json"           -d '{"date":"2025-11-05","appointment_type":"consultation"}' | python -m json.tool

echo "\nTesting booking"
curl -s -X POST "http://127.0.0.1:8000/api/calendly/book"           -H "Content-Type: application/json"           -d '{
    "appointment_type":"consultation",
    "date":"2025-11-05",
    "start_time":"11:00",
    "patient":{"name":"John Doe","email":"john@example.com","phone":"+1-555-0100"},
    "reason":"Checkup"
  }' | python -m json.tool
