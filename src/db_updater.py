import pandas as pd
import sqlite3 as sql

# Conecte-se ao banco de dados
database = sql.connect('./src/database/database.db')

def add_column_if_not_exists(cursor, column_name, column_type):
    # Verifica se a coluna já existe
    cursor.execute(f"PRAGMA table_info(stocks)")
    columns = [column[1] for column in cursor.fetchall()]
    if column_name not in columns:
        # Adiciona a coluna se não existir
        cursor.execute(f"ALTER TABLE stocks ADD COLUMN {column_name} {column_type}")

def update_stock_prices(csv_file):
    # Leia o arquivo CSV e converta o separador decimal de ',' para '.'
    df = pd.read_csv(csv_file, converters={'price_2024': lambda x: x.replace(',', '.')})

    with database:
        cursor = database.cursor()
        
        # Adiciona a coluna price_2024 se não existir
        add_column_if_not_exists(cursor, "price_2024", "TEXT")

        for index, row in df.iterrows():
            ticker = row['ticker']
            price_2024 = row['price_2024']

            # Verifique se o ticker já existe no banco de dados
            cursor.execute("SELECT COUNT(*) FROM stocks WHERE ticker = ?", (ticker,))
            count = cursor.fetchone()[0]

            if count > 0:
                # Atualize o preço da ação para 2024
                cursor.execute("UPDATE stocks SET price_2024 = ?, time_last_modified = CURRENT_TIMESTAMP WHERE ticker = ?", (price_2024, ticker))
            else:
                # Insira um novo registro se o ticker não existir
                cursor.execute("INSERT INTO stocks (ticker, price_2024, time_last_modified) VALUES (?, ?, CURRENT_TIMESTAMP)", (ticker, price_2024))

        database.commit()

if __name__ == "__main__":
    csv_file = './src/update/price_2024.csv'  # Substitua pelo caminho do seu arquivo CSV
    update_stock_prices(csv_file)
    print("Atualização concluída com sucesso!")