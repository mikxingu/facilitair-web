from typing import List
import sqlite3 as sql

database = sql.connect('./src/database/database.db')

def get_stocks_db():
    """
    Retorna todos os tickers cadastrados no banco
    """
    with database:
        cursor = database.cursor()
        cursor.execute("SELECT ticker FROM stocks ")
        stocks = cursor.fetchall()
        list = []
        for item in stocks:
            list.append(item[0]) #TRANSFORMA A TUPLA RETORNADA PELO DB EM LISTA.
        return list
@staticmethod
def get_stock_information(ticker: str, year: int):
    """
    Retorna os dados do ticker informado
    """
    with database:
        cursor = database.cursor()
        price_column = f"price_{year}"
        query = f"SELECT type, cnpj, razao_social, {price_column} FROM stocks WHERE ticker = ?"
        cursor.execute(query, (ticker,))
        stock = cursor.fetchone()
        return stock