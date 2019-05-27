# luizalabs_test

Tecnologias utilizadas:
Python 3.7,
Django 2.2.1,
Django rest framework,
PostgreSQL,
Docker,
Docker-Compose


### Para rodar os testes da aplicação:
```shell 
python labs_test/manage.py migrate
```


### Para startar a aplicação basta digitar :
```shell 
docker-compose up -d
```

### Para acessar o Admin:
```shell 
http://localhost:8000/admin

login: admin
senha: admin

usuario super previamente cadastrado via migration

```

### API da aplicação
```shell 
http://localhost:8000/employee
    POST /employee
    body
    {
        'name': 'string',
        'email': 'string',
        'department': 'string'
    }

    GET /employee
    response
    [{
        'name': 'string',
        'email': 'string',
        'department': 'string'
    }]

    GET /employee/<id>
    response
    {
        'name': 'string',
        'email': 'string',
        'department': 'string'
    }

    PUT /employee/<id>
    body
    {
        'name': 'string',
        'email': 'string',
        'department': 'string'
    }
    response
    {
        'name': 'string',
        'email': 'string',
        'department': 'string'
    }

    DELETE /employee/<id>
```


