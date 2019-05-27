# luizalabs_test

tecnologias utilizadas
Python 3.7
Django 2.2.1
Django rest framework

### Para rodar os testes da aplicação:
```shell 
python labs_test/manage.py migrate
```


### Para startar a aplicação basta digitar :
```shell 
docker-compose up -d
```

### Rotas possíveis da aplicação
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


