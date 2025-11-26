Feature: Teste da API de Fotos (jsonplaceholder /photos)
  Como um usuário de testes
  Eu quero verificar as funcionalidades básicas do endpoint /photos

  Scenario: 1. Leitura de Coleção e Estrutura
    Given a URL base da API
    When eu faço uma requisição GET para o endpoint "/photos"
    Then o status code deve ser 200
    And o corpo da resposta deve ser uma lista
    And o primeiro item da lista deve conter a chave "id"

  Scenario: 2. Leitura de Recurso Específico (ID 2)
    Given a URL base da API
    When eu faço uma requisição GET para o endpoint "/photos/2"
    Then o status code deve ser 200
    And o campo "id" da resposta deve ser 2

  Scenario: 3. Criação de Novo Item (POST)
    Given a URL base da API
    And o corpo da requisição é um novo post
    When eu faço uma requisição POST para o endpoint "/photos"
    Then o status code deve ser 201
    And o corpo da resposta deve conter a chave "id"

  Scenario: 4. Filtragem por albumId=1
    Given a URL base da API
    When eu faço uma requisição GET para o endpoint "/photos?albumId=1"
    Then o status code deve ser 200
    And todos os itens da lista devem ter o campo "albumId" igual a 1

  Scenario: 5. Atualização Parcial de Recurso (PATCH)
    Given a URL base da API
    And o corpo da requisição é a atualização do titulo
    When eu faço uma requisição PATCH para o endpoint "/photos/3"
    Then o status code deve ser 200
    And o campo "title" da resposta deve ser "Novo Título Teste Gherkin"