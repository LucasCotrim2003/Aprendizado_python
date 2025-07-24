import sqlite3
from sqlite3 import Error

def criar_conexao(db_file):
    """Cria uma conexão com o banco de dados SQLite."""
    conexao = None
    try:
        conexao = sqlite3.connect(db_file)
        print(f"Conexão com o banco de dados {db_file} estabelecida.")
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return conexao

def executar_query(conexao, query, params=None):

    try:
        cursor = conexao.cursor()
        if params:
            cursor.execute(query,params)
        else:
            cursor.execute(query)
            conexao.commit()
        print("Query executada com sucesso.")
    except Error as e:
        print(f"Erro ao executar a query: {e}")

def fechar_conexao(conexao):
    """Fecha a conexão com o banco de dados."""
    if conexao:
        conexao.close()
        print("Conexão com o banco de dados fechada.")

