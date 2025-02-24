import pytest
import requests

# URL da FakeStore API
FAKE_STORE_URL = "localhost:8000/docs#"

# Teste de GET para produtos
def test_get_fake_store_produtos():
    response = requests.get(FAKE_STORE_URL)
    
    # Verificar se a resposta tem status code 200
    assert response.status_code == 200
    
    # Verificar se a resposta é uma lista
    produtos = response.json()
    assert isinstance(produtos, list)
    
    # Verificar se existem produtos na resposta
    assert len(produtos) > 0
