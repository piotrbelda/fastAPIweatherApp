from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates("templates")

@router.get('/')
def home(request: Request):
    return templates.TemplateResponse('template.html', context={"request": request})