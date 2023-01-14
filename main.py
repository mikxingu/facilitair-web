from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()

@app.get("/")
async def get_root():
    return "Hello!"