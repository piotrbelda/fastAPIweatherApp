from typing import List
from models.location import Location
from models.reports import Report
import datetime
import uuid

__reports: List[Report] = []

async def get_reports() -> List[Report]:
    return list(__reports)

def add_report(description: str, location: Location) -> Report:
    now = datetime.datetime.now()
    report = Report(id=str(uuid.uuid4()), location=location, description=description, created_date=now)
    __reports.append(report)
    __reports.sort(key=lambda x: x.created_date, reverse=True)
    return report