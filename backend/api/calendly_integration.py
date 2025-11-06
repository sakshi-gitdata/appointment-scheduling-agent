from fastapi import APIRouter, HTTPException
from ..models.schemas import AvailabilityRequest, AvailabilityResponse, Slot, BookingRequest, BookingResponse
from ..utils.booking_store import load_schedule, add_booking
from datetime import datetime
import uuid

router = APIRouter(prefix="/api/calendly", tags=["calendly"])

def time_str_to_minutes(t):
    h, m = map(int, t.split(":"))
    return h*60 + m

def minutes_to_time_str(m):
    h = m // 60
    mm = m % 60
    return f"{h:02d}:{mm:02d}"

@router.post("/availability", response_model=AvailabilityResponse)
def get_availability(req: AvailabilityRequest):
    schedule = load_schedule()
    date = req.date
    try:
        dt = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format, use YYYY-MM-DD")
    day = dt.strftime("%A").lower()
    hours = schedule.get("working_hours", {}).get(day)
    if not hours:
        return AvailabilityResponse(date=date, available_slots=[])

    booked = [a for a in schedule.get("appointments", []) if a.get("date") == date]
    duration = schedule.get("slot_durations", {}).get(req.appointment_type, 30)

    slots = []
    for period in hours:
        start_s, end_s = period.split("-")
        start = time_str_to_minutes(start_s)
        end = time_str_to_minutes(end_s)
        t = start
        while t + duration <= end:
            st = minutes_to_time_str(t)
            en = minutes_to_time_str(t + duration)
            conflict = any(not (en <= b["start_time"] or st >= b["end_time"]) for b in booked)
            slots.append(Slot(start_time=st, end_time=en, available=(not conflict)))
            t += duration
    return AvailabilityResponse(date=date, available_slots=slots)

@router.post("/book", response_model=BookingResponse)
def book_appointment(req: BookingRequest):
    schedule = load_schedule()
    try:
        dt = datetime.strptime(req.date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format")
    day = dt.strftime("%A").lower()
    hours = schedule.get("working_hours", {}).get(day)
    if not hours:
        raise HTTPException(status_code=400, detail="Doctor not available on this date")

    def overlap(s1,e1,s2,e2):
        return not (e1 <= s2 or s1 >= e2)

    for ap in schedule.get("appointments", []):
        if ap.get("date") == req.date and overlap(req.start_time, req.start_time, ap["start_time"], ap["end_time"]):
            raise HTTPException(status_code=400, detail="Slot already booked")

    booking_id = f"APPT-{uuid.uuid4().hex[:8]}"
    confirmation_code = uuid.uuid4().hex[:6].upper()
    booking = {
        "booking_id": booking_id,
        "status": "confirmed",
        "confirmation_code": confirmation_code,
        "details": {
            "appointment_type": req.appointment_type,
            "date": req.date,
            "start_time": req.start_time,
            "patient": req.patient.dict(),
            "reason": req.reason
        },
        "date": req.date,
        "start_time": req.start_time,
        "end_time": req.start_time
    }
    add_booking(booking)
    return BookingResponse(booking_id=booking_id, status="confirmed", confirmation_code=confirmation_code, details=booking["details"])
