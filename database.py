import mysql.connector
import os
from dotenv import load_dotenv
# Configuração da conexão
# Carregar variáveis do .env
load_dotenv()
# Configuração da conexão usando as variáveis do .env
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        auth_plugin=os.getenv("DB_AUTH_PLUGIN")
    )