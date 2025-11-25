import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_update_post():
    payload = {"title": "Título Atualizado"}
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Título Atualizado"