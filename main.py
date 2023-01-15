from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from src.routers import stocks

### SQL



app = FastAPI()

@app.get("/")
async def get_root():
    return "Hello!"

app.include_router(stocks.router)