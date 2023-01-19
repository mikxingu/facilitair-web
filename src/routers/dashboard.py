from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from src.services import StocksService

router = APIRouter(prefix='/dashboard', tags=['dashboard'])

stocks_all = StocksService.get_stocks_db()

templates = Jinja2Templates(directory='./src/templates')
@router.get('')
def show_dashboard(request: Request):
    """Abre o dashboard de lançamento de ações"""
    return templates.TemplateResponse('dashboard.html',  {
        'request': request,
        'all_stocks': stocks_all
    })