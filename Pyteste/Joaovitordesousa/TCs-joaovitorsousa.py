import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

# Teste 1: Obter todos os posts (GET)
def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]

# Teste 2: Obter um post específico (GET)
def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data

# Teste 3: Criar um novo post (POST)
def test_create_post():
    payload = {"title": "Novo Post", "body": "Corpo do post", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Novo Post"
    assert "id" in data

# Teste 4: Atualizar um post (PUT)
def test_update_post():
    payload = {"title": "Título Atualizado"}
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Título Atualizado"

# Teste 5: Deletar um post (DELETE)
def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200