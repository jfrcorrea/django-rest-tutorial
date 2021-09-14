# django-rest-tutorial
Django REST framework Quickstart tutorial

https://www.django-rest-framework.org/tutorial/quickstart/#quickstart

# Execução
Para executar este projeto, acesse o diretório "tutorial" e execute o seguinte comando:

```bash
$ docker-compose up
```

# Endpoints
Fora os endpoints exibidos na tela inicial, que são:
- "users": "http://127.0.0.1:8000/users/"
- "groups": "http://127.0.0.1:8000/groups/"
- "chucknorrisjokes": "http://127.0.0.1:8000/chucknorrisjokes/"

Existe o endpoint "get-chuck-norris-joke", que retorna uma piada aleatória, acessada pela url https://api.chucknorris.io/jokes/random.

Cada acesso a este último endpoint, salva a piada em uma tabela do banco de dado, que pode ser consultada pelo endpoint "chucknorrisjokes".