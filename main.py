from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from views import home
from api import weather_api
from pathlib import Path
import json
from services import openweather_service

app = FastAPI()

def configure_routing():
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(home.router)
    app.include_router(weather_api.router)

def configure_api_keys():
    file = Path("settings.json").absolute()
    if not file.exists():
        print(f"Warning!: {file} file not found...")
        raise Exception("settings.json not found")
    with open("settings.json") as fin:
        settings = json.load(fin)
        openweather_service.api_key = settings.get("api_key")

def configure():
    configure_routing()
    configure_api_keys()

if __name__ == "__main__":
    configure()
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    configure()