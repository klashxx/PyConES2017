
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

[![permissions][asciicast-04_permissions-png]][asciicast-04_permissions-url]

#### Uso

Con los *fixtures* del código de instalación genera un nuevo usuario `test` que se autentica con la contraseña `PyConES17`.

A este usuario se le otorga la pertenencia al grupo  `pycones_g` que a su vez tiene permisos de get sobre la [*API*][metricas-drf].

Podemos observar como unicamente podemos consultar estos datos *logeandonos* con el *super-usuario* o con *test*.

En el `views.py` se diferencia la gestión de permisos del acceso a la vista y del *viewset*.

Sin embargo `requests` no tiene acceso a los datos de contexto necesario para acceder a la password de sesión, por lo que no resulta practico usar este modulo para extraer los datos de la API, el lugar natural para esto es el *template* como veremos en el próximo paso.

[asciicast-04_permissions-png]: https://asciinema.org/a/vwUNgut3NchCKmeO3VKqALqFq.png
[asciicast-04_permissions-url]: https://asciinema.org/a/vwUNgut3NchCKmeO3VKqALqFq

[metricas-drf]: http://0.0.0.0/metrics/api/v1/metricas/

[localhost]: http://0.0.0.0/
