from fastapi import APIRouter

router = APIRouter(prefix="/stock", tags=["stock"])

@router.get("/{ticker}")
async def get_single_stock(ticker: str):
    """
    Retorna informações da ação para o ticker informado.
    """
    # TODO - CRIAR SERVIÇO NO BANCO PARA FAZER UMA QUERY PARA UMA AÇÃO ESPECÍFICA.
    return ticker   