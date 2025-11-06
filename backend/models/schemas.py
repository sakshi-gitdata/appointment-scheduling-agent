from pydantic import BaseModel, EmailStr
from typing import Optional, List

class AvailabilityRequest(BaseModel):
    date: str  # YYYY-MM-DD
    appointment_type: Optional[str] = "consultation"

class Slot(BaseModel):
    start_time: str
    end_time: str
    available: bool

class AvailabilityResponse(BaseModel):
    date: str
    available_slots: List[Slot]

class Patient(BaseModel):
    name: str
    email: EmailStr
    phone: str

class BookingRequest(BaseModel):
    appointment_type: str
    date: str  # YYYY-MM-DD
    start_time: str  # HH:MM
    patient: Patient
    reason: Optional[str] = None

class BookingResponse(BaseModel):
    booking_id: str
    status: str
    confirmation_code: str
    details: dict
