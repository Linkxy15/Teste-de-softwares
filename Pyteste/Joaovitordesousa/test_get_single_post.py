import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data