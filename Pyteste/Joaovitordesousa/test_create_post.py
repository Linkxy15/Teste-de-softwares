import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_create_post():
    payload = {"title": "Novo Post", "body": "Corpo do post", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Novo Post"
    assert "id" in data
