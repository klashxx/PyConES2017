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

[![frontend][asciicast-05_frontend-png]][asciicast-05_frontend-url]

#### Uso

La apariencia de la web cambia totalmente al aplicar [*Bootstrap*][bootstrap] como se puede comprobar en cualquiera de sus [vistas][localhost].

El[template][metrics-template] de la aplicación métricas habla directamente mediante [*jQuery*][jquery-get] con la [*API*][metricas-drf] extrae los datos y los renderiza mediante [*Vue*][vue-js].

[localhost]: http://0.0.0.0/
[asciicast-05_frontend-png]: https://asciinema.org/a/137086.png
[asciicast-05_frontend-url]: https://asciinema.org/a/137086
[metricas-drf]: http://0.0.0.0/metrics/api/v1/metricas/
[metrics-template]: https://github.com/klashxx/PyConES2017/blob/05_frontend/web/sysgate/apps/metrics/templates/metrics/home.html
[bootstrap]: http://getbootstrap.com/
[jquery-get]: https://api.jquery.com/jquery.get/
[vue-js]: https://vuejs.org/
