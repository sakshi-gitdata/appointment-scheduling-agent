from fastapi import FastAPI
from .api.calendly_integration import router as calendly_router

app = FastAPI(title="Appointment Scheduling Agent - Mock Calendly")

app.include_router(calendly_router)

@app.get("/")
def root():
    return {"message": "Appointment Scheduling Agent - Mock Calendly API"}
