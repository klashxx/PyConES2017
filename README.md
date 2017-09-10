### 02. Aplicaciones

#### Instalación

Branch: [`02_apps`](https://github.com/klashxx/PyConES2017/tree/02_apps)

```
$ git checkout 02_apps
$ docker-compose stop
$ docker-compose build
$ docker-compose up -d
$ docker-compose exec sysgate python manage.py migrate
$ docker-compose exec sysgate python manage.py loaddata sysgate/fixtures/metrics.metrica.json
```

[![usuarios][asciicast-02_apps-png]][asciicast-02_apps-url]

#### Uso

Abre [localhost][localhost], *logeate* con el usuario creado en [`01_auth`](https://github.com/klashxx/PyConES2017/tree/01_auth) y accede a la aplicación *Métricas*.

Cuando termines las pruebas continúa por [*aquí*](https://github.com/klashxx/PyConES2017/tree/03_drf).

[asciicast-02_apps-png]: https://asciinema.org/a/133221.png
[asciicast-02_apps-url]: https://asciinema.org/a/133221

[localhost]: http://0.0.0.0/
