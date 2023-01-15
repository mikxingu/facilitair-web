from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix='/dashboard', tags=['dashboard'])

templates = Jinja2Templates(directory='./src/templates')
@router.get('')
def show_dashboard(request: Request):
    """Abre o dashboard de lançamento de ações"""
    return templates.TemplateResponse('dashboard.html',  {
        'request': request
    })