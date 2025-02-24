from database import get_db_connection  # Importando a conexão com o MySQL
# função para conectar no banco será utilizada como importe dentro do arquivo service.py
def conectar():
        conexao_db = get_db_connection()
        return conexao_db