#imports
from fastapi import FastAPI
from schemas.schemas import ProductSchema
from typing import List
from services.service import carregar_produtos, obtem_produtos, get_by_categoria
# iniciliza a aplicacao
app = FastAPI()
# Endpoint para carregar dados da FakeStoreAPI para o MySQL
@app.post(
    "/produtos",
    tags=["Produtos"],  # Nome da categoria no Swagger
    description="Este endpoint carrega os dados da FakeStoreAPI e os armazena no MySQL."
)
def produtos_post():
     return carregar_produtos()
 
# Endpoint para buscar os produtos da base Mysql e retornar para a api
@app.get("/produtos",
    tags=["Produtos"],  # Nome da categoria no Swagger
    description="Este endpoint é um get de produtos que busca na base MySQL.")
def produtos_get() -> List[ProductSchema]:
    return obtem_produtos()

# Endpoint para buscar os produtos da base Mysql e retornar para a api
@app.get("/produtos/{categoria}",
    tags=["Produtos"],  # Nome da categoria no Swagger
    description="Este endpoint é um get de produtos por categoria")
def produtos_get_by_categoria(categoria: str) -> List[ProductSchema]:
    return get_by_categoria(categoria)
