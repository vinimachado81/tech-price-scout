import sqlite3
import os

DB_PATH = 'data/db/precos.db'

def conectar():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)

def setup_db():
    conn = conectar()
    cursor = conn.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS historico_precos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT NOT NULL,
        loja TEXT NOT NULL,
        preco REAL NOT NULL,
        data_coleta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    cursor.execute(sql)
    conn.commit()
    conn.close()

def salvar_dados(dados_limpos):
    if not dados_limpos:
        return

    conn = conectar()
    cursor = conn.cursor()
    
    print(f"💾 Salvando {len(dados_limpos)} registros no banco...")

    for item in dados_limpos:
        cursor.execute("""
            INSERT INTO historico_precos (produto, loja, preco)
            VALUES (?, ?, ?)
        """, (item['produto'], item['loja'], item['preco']))
    
    conn.commit()
    conn.close()
    print("✅ Dados salvos!")