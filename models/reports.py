from pydantic import BaseModel
import datetime
from typing import Optional
from models.location import Location

class ReportSubmittal(BaseModel):
    description: str
    location: Location

class Report(ReportSubmittal):
    id: str
    created_date: Optional[datetime.datetime]