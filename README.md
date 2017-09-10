### 03. DRF

#### Instalación

Branch: [`03_drf`](https://github.com/klashxx/PyConES2017/tree/03_drf)

```
$ git checkout 03_drf
$ docker-compose stop
$ docker-compose build sysgate
$ docker-compose up -d
$ docker-compose exec sysgate python manage.py collectstatic --noinput
```

[![drf][asciicast-03_drf-png]][asciicast-03_drf-url]

#### Uso

Apunta el *browser* sobre la interfaz de consulta de [*DRF*][metricas-drf] para visualizar la *API* que extrae los datos almacenados en el modelo [`Metrica`](https://github.com/klashxx/PyConES2017/blob/03_drf/web/sysgate/apps/metrics/models.py).

Ejemplo de filtrado por [*tipo*][metricas-drf-filter].

Abre la aplicación [*métricas*][metricas] que ahora se alimenta directamente de la *API REST*.

Al finalizar pasa a la siguiente [*rama*](https://github.com/klashxx/PyConES2017/tree/04_permissions).

[asciicast-03_drf-png]: https://asciinema.org/a/133252.png
[asciicast-03_drf-url]: https://asciinema.org/a/133252

[localhost]: http://0.0.0.0/
[metricas]: http://0.0.0.0/metrics/
[metricas-drf]: http://0.0.0.0/metrics/api/v1/metricas/
[metricas-drf-filter]: http://0.0.0.0/metrics/api/v1/metricas/?tipo=d
