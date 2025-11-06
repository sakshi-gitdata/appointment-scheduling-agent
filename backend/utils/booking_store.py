import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / "data"
SCHEDULE_FILE = BASE / "doctor_schedule.json"

def load_schedule():
    with open(SCHEDULE_FILE, "r") as f:
        return json.load(f)

def save_schedule(schedule):
    with open(SCHEDULE_FILE, "w") as f:
        json.dump(schedule, f, indent=2)

def add_booking(booking):
    schedule = load_schedule()
    schedule.setdefault("appointments", []).append(booking)
    save_schedule(schedule)
    return booking
