#pagetest_get_all_posts.py
Feature:  Obter todos os post

  Scenario: Acesso bem sucedido a todos os post 
          Dado que o usuário está na pagina inicial 
          Quando o usuario navega para a pagina inicial
          E acessa acessa os recursos 
          Então abre uma aba com todos os posts

#pagetest_get_single_post.py
Feature:  Obter um post específico
  Scenario: Acesso bem sucedido a um post específico
          Dado que o usuário está na pagina inicial 
          Quando o usuario navega para a pagina inicial
          E acessa acessa as rotas 
          Então obtem um post específico

#pagetest_create_post.py
Feature:  Criar um novo post          
  Scenario: Acesso bem sucedido a criação de um post
          Dado que o usuário está na pagina inicial 
          Quando o usuario navega para a pagina inicial
          E acessa acessa as rotas 
          Então Cria seu proprio post

#pagetest_update_post.py
Feature: Atualizar um post
  Scenario: Acesso bem sucedido a atualização de um post
          Dado que o usuário está na pagina inicial 
          Quando o usuario navega para a pagina inicial
          E acessa acessa as rotas 
          Então Atualiza um post 

#pagetest_delete_post.py
Feature:  Deletar um post
  Scenario: Acesso bem sucedido a exclusão de um post
          Dado que o usuário está na pagina inicial 
          Quando o usuario navega para a pagina inicial
          E acessa acessa as rotas 
          Então exclui um post 