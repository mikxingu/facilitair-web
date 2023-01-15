from fastapi import APIRouter, Request, Depends, BackgroundTasks
from requests import Session

###SQL
# import sqlite3 as sql
# database = sql.connect('./src/database/database.db')

# def get_stocks_db():

#     with database:
#         cursor = database.cursor()
#         cursor.execute("SELECT ticker FROM stocks ")
#         stocks = cursor.fetchall()
#         return stocks
    

router = APIRouter(prefix="/stocks", tags=['stocks'])

@router.get("")
async def get_all_stocks():
    """
    Recupera todos os tickers cadastrados no banco
    """
    # tickers = get_stocks_db()
    tickers = ["AABC3"]
    return tickers

@router.get("/{ticker}")
async def get_all_stocks(ticker: str):
    """
    Retorna informações da ação para o ticker informado.
    """
    # TODO - CRIAR SERVIÇO NO BANCO PARA FAZER UMA QUERY PARA UMA AÇÃO ESPECÍFICA.
    return ticker   