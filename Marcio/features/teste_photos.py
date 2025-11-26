import requests
import pytest
from pytest_bdd import scenarios, given, when, then


scenarios('features/photos.feature')


BASE_URL = "https://jsonplaceholder.typicode.com"



@pytest.fixture
def context():
    """Fixture para armazenar dados compartilhados entre os passos."""
    return {}

@given('a URL base da API')
def url_base(context):
    context["base_url"] = BASE_URL

@given('o corpo da requisição é um novo post')
def new_post_body(context):
    context["data"] = {
        "albumId": 101,
        "title": "Foto do Teste de Criação Gherkin",
        "url": "http://novo.url.com/600/teste",
        "thumbnailUrl": "http://novo.url.com/150/teste"
    }

@given('o corpo da requisição é a atualização do titulo')
def update_patch_body(context):
    context["data"] = {
        "title": "Novo Título Teste Gherkin"
    }



@when('eu faço uma requisição GET para o endpoint "{endpoint}"')
def send_get_request(context, endpoint):
    url = context["base_url"] + endpoint
    context["response"] = requests.get(url)

@when('eu faço uma requisição POST para o endpoint "{endpoint}"')
def send_post_request(context, endpoint):
    url = context["base_url"] + endpoint
    data = context.get("data", {})
    context["response"] = requests.post(url, json=data)

@when('eu faço uma requisição PATCH para o endpoint "{endpoint}"')
def send_patch_request(context, endpoint):
    url = context["base_url"] + endpoint
    data = context.get("data", {})
    context["response"] = requests.patch(url, json=data)



@then('o status code deve ser {status_code:d}')
def check_status_code(context, status_code):
    assert context["response"].status_code == status_code

@then('o corpo da resposta deve ser uma lista')
def check_response_is_list(context):
    assert isinstance(context["response"].json(), list)

@then('o primeiro item da lista deve conter a chave "id"')
def check_first_item_keys(context):
    data = context["response"].json()
    assert len(data) > 0
    assert "id" in data[0]
    
@then('o campo "id" da resposta deve ser {expected_id:d}')
def check_specific_id(context, expected_id):
    data = context["response"].json()
    assert data["id"] == expected_id

@then('o corpo da resposta deve conter a chave "id"')
def check_id_in_body(context):
    data = context["response"].json()
    assert "id" in data

@then('todos os itens da lista devem ter o campo "albumId" igual a {expected_album_id:d}')
def check_all_album_ids(context, expected_album_id):
    data = context["response"].json()
    
    assert len(data) > 0
   
    for item in data:
        assert item["albumId"] == expected_album_id

@then('o campo "title" da resposta deve ser "{expected_title}"')
def check_updated_title(context, expected_title):
    data = context["response"].json()
    assert data["title"] == expected_title