from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from src.routers import stock, dashboard

tags_metadata = [{
    'name':'stocks',
    'description':'Operações com lotes de ações'
},{
    'name': 'stock',
    'description': 'Operações com ação unica'
}
]

app = FastAPI(openapi_tags=tags_metadata,
              version='1.3.1')

templates = Jinja2Templates(directory='./src/templates')

@app.get("/")
def home(request: Request):
    """Abre a pagina home do app"""
    return templates.TemplateResponse('home.html',{
        'request': request
    })

app.include_router(stock.router)
app.include_router(dashboard.router)