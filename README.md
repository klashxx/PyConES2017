
### 04. Permisos

#### Instalación

Branch: [`04_permissions`](https://github.com/klashxx/PyConES2017/tree/04_permissions)

```
$ git checkout 04_permissions
$ docker-compose stop
$ docker-compose build sysgate
$ docker-compose up -d
$ docker-compose exec sysgate python manage.py migrate account
$ docker-compose exec sysgate python manage.py loaddata sysgate/fixtures/auth.group.json
$ docker-compose exec sysgate python manage.py loaddata sysgate/fixtures/account.user.json
```

[localhost]: http://0.0.0.0/
