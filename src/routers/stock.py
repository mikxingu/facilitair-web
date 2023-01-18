from fastapi import APIRouter
from src.services import StocksService


router = APIRouter(prefix="/stock", tags=["stock"])

@router.get("/{ticker}")
async def get_single_stock(ticker: str):
    """
    Retorna informações da ação para o ticker informado.
    """
    query_ticker = ticker.upper()
    return StocksService.get_stock_information(query_ticker)