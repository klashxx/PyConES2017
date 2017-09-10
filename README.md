
# :warning: WARNING: WORK IN PROGRESS :warning:

## :snake: Sysadmin vs Django
[![][license-svg]][license-url]

Código base que ilustrará la charla [*Sysadmin vs Django*](https://2017.es.pycon.org/es/schedule/sysadmin-vs-django/) en la [PyConES Cáceres 2017](http://2017.es.pycon.org/).

### ¿Sobre que hablaremos?

Basado en una historia real xP … se mostrará como es posible desarrollar una *webapp* con `Python` + `Django` afrontando un deadline ajustado y sin experiencia previa en desarrollo web.

Este proyecto se convirtió en una experiencia altamente gratificante aunque no exenta de escollos, solventados con mayor o menor fortuna. Precisamente estos tips prácticos serán los que protagonicen la charla con un objetivo claro, intentar facilitar el transito del novato al mundo Django.

El repositorio se estructura en [*ramas*](https://git-scm.com/docs/git-branch), usándose cada una de ellas para ilustrar un tema en concreto.

### Pruébalo en tu equipo

Todo el software se ha *dockerizado* de forma que la aplicación pueda levantarse independientemente del entorno del usuario.

En cada rama se detallan las instrucciones de instalación.

**Vale, basta de charla and ... Show me the code** :godmode:


[01](#usuarios). Usuarios

[02](#aplicaciones). Aplicaciones

[03](#drf). DRF

[04](#permissions). Permisos

<br>

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

[![usuarios][asciicast-01_auth-png]][asciicast-01_auth-url]

#### Uso

Apunta tu navegador al [localhost][localhost], registra un usuario y prueba las diferentes opciones de *autenticación*.

### 02. Aplicaciones

#### Instalación

Branch: [`02_apps`](https://github.com/klashxx/PyConES2017/tree/02_apps)

```
$ git checkout 02_apps
$ docker-compose stop
$ docker-compose build sysgate
$ docker-compose up -d
$ docker-compose exec sysgate python manage.py migrate
$ docker-compose exec sysgate python manage.py loaddata sysgate/fixtures/metrics.metrica.json
```

[![apps][asciicast-02_apps-png]][asciicast-02_apps-url]

#### Uso

Abre [localhost][localhost], *logeate* con el usuario creado en [`01_auth`](https://github.com/klashxx/PyConES2017/tree/01_auth) y accede a la aplicación *Métricas*.

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

### 04. Permisos

#### Instalación

Branch: [`04_permissions`](https://github.com/klashxx/PyConES2017/tree/04_permissions)

```
$ git checkout 04_permissions
$ docker-compose stop
$ docker-compose build sysgate
$ docker-compose up -d
```

### Contacta conmigo

Mis perfiles online están [**aquí**](https://klashxx.github.io/about), no te cortes ... :godmode:

<h6 align="center">
<a href="https://2017.es.pycon.org/es/schedule/sysadmin-vs-django/">
  <img src="https://github.com/klashxx/PyConES2017/blob/03_drf/web/sysgate/static/img/logo_pycones17.png">
</a></h6>
<br>
<h6 align="center">Made with :heart: in Almería, Spain.</h6>

[license-svg]: https://img.shields.io/badge/license-MIT-blue.svg
[license-url]: https://opensource.org/licenses/MIT

[asciicast-01_auth-png]: https://asciinema.org/a/133244.png
[asciicast-01_auth-url]: https://asciinema.org/a/133244

[asciicast-02_apps-png]: https://asciinema.org/a/133221.png
[asciicast-02_apps-url]: https://asciinema.org/a/133221

[asciicast-03_drf-png]: https://asciinema.org/a/133252.png
[asciicast-03_drf-url]: https://asciinema.org/a/133252

[localhost]: http://0.0.0.0/
[metricas]: http://0.0.0.0/metrics/
[metricas-drf]: http://0.0.0.0/metrics/api/v1/metricas/
[metricas-drf-filter]: http://0.0.0.0/metrics/api/v1/metricas/?tipo=d
