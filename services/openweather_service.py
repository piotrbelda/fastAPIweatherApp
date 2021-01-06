from typing import Optional
from infrastructure import weather_cache
import httpx
from models.validation_error import ValidationError
from fastapi import Response

api_key: Optional[str] = None

async def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    forecast = weather_cache.get_weather(city, state, country, units)
    if forecast:
        return forecast
    if state:
        q = f"{city},{state},{country}"
    else:
        q = f"{city},{country}"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&units={units}&appid={api_key}"
    async with httpx.AsyncClient() as client:
        response: Response = await client.get(url)
        if response.status_code != 200:
            raise ValidationError(response.text, status_code=response.status_code)
        response.raise_for_status()
    data = response.json()
    forecast = data["main"]

    weather_cache.set_weather(city, state, country, units, forecast)

    return forecast