import pytest
import requests

# Base URL da sua API FastAPI
BASE_URL = "http://localhost:8000/docs#/"

# Teste GET para listar produtos
def test_get_produtos():
    response = requests.get(f"{BASE_URL}/produtos")
    assert response.status_code == 200
    produtos = response.json()
    assert isinstance(produtos, list)  # Verificar se é uma lista
    assert len(produtos) > 0  # Verificar se retornou produtos

# Teste POST para adicionar um novo produto
def test_post_produtos():
    novo_produto = {
        "title": "Produto Teste",
        "price": 29.99,
        "category": "Test Category",
        "description": "Descrição do produto de teste",
        "image": "https://link_da_imagem.com"
    }

    response = requests.post(f"{BASE_URL}/produtos", json=novo_produto)
    assert response.status_code == 201
    produto = response.json()
    assert produto["title"] == novo_produto["title"]
    assert produto["price"] == novo_produto["price"]
