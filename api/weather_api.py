from typing import Optional, List
from fastapi import APIRouter, Depends, Form, Response
from pydantic import BaseModel
from services import openweather_service, report_service
from models.validation_error import ValidationError
from models.reports import Report
from models.location import Location

router = APIRouter()

@router.get("/api/weather/{city}")
async def weather(location: Location = Depends(), units: Optional[str] = "metric"):
    try:
        return await openweather_service.get_report(location.city, location.state, location.country, units)
    except ValidationError as ve:
        return Response(content=ve.error_msg, status_code=ve.status_code)

@router.post('/api/weather/search')
async def searchWeather(city: str = Form(...), state: str = Form(None), country: str = Form("POL") , units: Optional[str] = "metric"):
    report = await openweather_service.get_report(city, state, country, units)
    return report

@router.get("/api/reports", name="all_reports")
async def reports_get() -> List[Report]:
    report_service.add_report("A raport", Location(city="Tarnow"))
    report_service.add_report("B report", Location(city="Warszawa"))
    return await report_service.get_reports()

@router.post("/api/reports", name="add_report")
async def reports_get(report_submittal: Report) -> Report:
    d = report_submittal.description
    loc = report_submittal.location
    return await report_service.add_report(d, loc)