### 06. Tricks

#### Instalación

Branch: [`06_tricks`](https://github.com/klashxx/PyConES2017/tree/06_tricks)

```
$ git checkout 06_tricks
$ docker-compose stop
$ docker-compose build sysgate
$ docker-compose up -d
$ docker-compose exec sysgate python manage.py collectstatic --noinput
```

[![tricks][asciicast-06_tricks-png]][asciicast-06_tricks-url]

#### Uso

Unos últimos trucos para terminar nuestra [*demo*][localhost]:

- Interfaz de navegación mediante [*breadcrumbs*][breadcrumbs-wikipedia].

- Menú *Acerca de*.

- Un nuevo [*admin*][admin-bootstrapped] más amigable basado en [*bootstrap*][bootstrap]. :point_right: Recuerda acceder con usuario de administración.

- Configuración del *logging*.

- Uso de la [*toolbar*][toolbar].

Juega el tiempo que quieras con la *web*, cuando termines puedes volver al [*master*](https://github.com/klashxx/PyConES2017#contacta-conmigo).

[localhost]: http://0.0.0.0/
[breadcrumbs-wikipedia]: https://es.wikipedia.org/wiki/Miga_de_pan_(inform%C3%A1tica)
[bootstrap]: http://getbootstrap.com/
[admin-bootstrapped]: http://0.0.0.0/admin/
[toolbar]: https://django-debug-toolbar.readthedocs.io/en/stable/
[asciicast-06_tricks-png]: https://asciinema.org/a/137215.png
[asciicast-06_tricks-url]: https://asciinema.org/a/137215
