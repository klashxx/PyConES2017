### 01. Usuarios

#### Instalación

Branch: [`01_auth`](https://github.com/klashxx/PyConES2017/tree/01_auth)

```
$ git clone https://github.com/klashxx/PyConES2017.git sysgate
$ cd sysgate/
$ git checkout 01_auth
$ docker-compose up -d
$ docker-compose exec sysgate python manage.py migrate
$ docker-compose exec sysgate python manage.py createsuperuser
```

[![Usuarios][asciicast-01_auth-png]][asciicast-01_auth-url]

#### Uso

Apunta tu navegador al [localhost][localhost], registra un usuario y prueba las diferentes opciones de *autenticación*.

Cuando estes list@ pasa al siguiente [*paso*](https://github.com/klashxx/PyConES2017/tree/02_apps)

[asciicast-01_auth-png]: https://asciinema.org/a/133244.png
[asciicast-01_auth-url]: https://asciinema.org/a/133244

[localhost]: http://0.0.0.0/
