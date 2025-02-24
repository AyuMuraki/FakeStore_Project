#ARQUIVO COM AS FUNÇÕES UTILIZADAS PELA API DE PRODUTOS
#imports
import requests
from repositorys.produto_repository import conectar
from datetime import datetime
from schemas.schemas import ProductSchema
from typing import List

#Busca os produtos na fakestore e processa o retorno (insere na base de dados).
def carregar_produtos():
    #busca dados na fakestore a partir do endpoint get - url/products
    resposta = requests.get("https://fakestoreapi.com/products")
    # se o status code da requição realizada foi sucesso (200) inicia o processamento
    if resposta.status_code == 200:
        # atribui o content body da resposta da requisição para a variavel produtos
        produtos: List[ProductSchema] = resposta.json()
        # abre uma conexao com o banco
        conexao = conectar()
        # cria um cursor
        cursor = conexao.cursor()
        #iteracao no array de produtos, para cada produto em produtos ira realizar um insert no banco de dados
        for produto in produtos:
            #cria a variavel timestamp que é a data hora exata de execucao, sera utilizado no comando de insert
            # formato yyyy-MM-dd hh-mm-ss
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #Criando comando de insert para cada produto para inserir os dados na tabela de produtos
            sql = """
                INSERT INTO produtos (id, title, price, category, description, image, timestamp)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                title = VALUES(title), 
                price = VALUES(price), 
                category = VALUES(category), 
                description = VALUES(description), 
                image = VALUES(image),
                timestamp = VALUES(timestamp)
            """
            valores = (
                str(produto["id"]), produto["title"], str(produto["price"]),
                produto["category"], produto["description"], produto["image"],
                timestamp
            )
            cursor.execute(sql, valores)
        #commita as alteracoes no banco efetivando todas as operacoes de insert
        conexao.commit()
        #encerra o cursor e fecha a conexao com o banco
        cursor.close()
        conexao.close()
        #retorna um objeto de mensagem caso tenha conseguido inserir tudo no banco
        return {"mensagem": "Produtos carregados no MySQL com sucesso!"}
    #retorna erro caso a resposta http (status_code) da requisição da fakestore não tenha sido 200
    return {"erro": "Erro ao acessar a API", "status_code": resposta.status_code}

#busca na base de dados e retorna um List[ProductSchema]
def obtem_produtos() -> List[ProductSchema]:
        # abre uma conexao com o banco
        conexao = conectar()
        # cria um cursor
        cursor = conexao.cursor()
        # monta consulta (query) que sera executada no banco de dados
        query = "SELECT id, title, price, category, description, image, timestamp FROM produtos;"
        # execução do comando no banco
        cursor.execute(query)
        resultado = cursor.fetchall()
        # transforma o resultado no banco em um List[ProductSchema]
        produtos = [ProductSchema(id=linha[0],
                                  title=linha[1],
                                  price=linha[2],
                                  category=linha[3],
                                  description=linha[4],
                                  image=linha[5],
                                  timestamp=linha[6]) for linha in resultado]
        # desaloca recursos e fecha conexão
        cursor.close()
        conexao.close()
        # retorna um List[ProductSchema]
        return produtos
    
def get_by_categoria(categoria: str) -> List[ProductSchema]:
        # abre uma conexao com o banco
        conexao = conectar()
        # cria um cursor
        cursor = conexao.cursor()
        # Define o script da procedure
        script = "CALL BuscarProdutosPorCategoria(%s)"
        produtos_resultado = []
        # Executa a procedure e itera sobre os resultados
        for result in cursor.execute(script, (categoria,), multi=True):
            if result.with_rows:  # Verifica se há um conjunto de resultados
                produtos = result.fetchall()  # Obtém os dados da consulta
                for produto in produtos:
                    #adiciona na lista de produtos_resultado
                    produtos_resultado.append(ProductSchema(id=produto[0],
                                  title=produto[1],
                                  price=produto[2],
                                  category=produto[3],
                                  description=produto[4],
                                  image=produto[5],
                                  timestamp=produto[6]))
                break #forca a saida do for superior
            else:
                break           
        # desaloca recursos e fecha conexão
        cursor.close()
        conexao.close()
        return produtos_resultado