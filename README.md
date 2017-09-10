
### 05. Frontend

#### Instalación

Branch: [`05_frontend`](https://github.com/klashxx/PyConES2017/tree/05_frontend)

```
$ git checkout 05_frontend
$ docker-compose stop
$ docker-compose build sysgate
$ docker-compose up -d
$ docker-compose exec sysgate python manage.py collectstatic --noinput
```

[localhost]: http://0.0.0.0/
