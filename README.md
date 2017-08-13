
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

<br>

### 01. Usuarios

#### Instalación

Branch: [`01_auth`](https://github.com/klashxx/PyConES2017/tree/01_auth)

```
$ git clone https://github.com/klashxx/PyConES2017.git sysgate
$ cd sysgate
$ git checkout 01_auth
$ docker volume create --name=data
$ docker-compose up -d
$ docker-compose exec sysgate python manage.py migrate
$ docker-compose exec sysgate python manage.py createsuperuser
```

[![usuarios][asciicast-01_auth-png]][asciicast-01_auth-url]

### Contacta conmigo

Mis perfiles online están [**aquí**](https://klashxx.github.io/about), no te cortes ... :godmode:

<h6 align="center">
<a href="https://2017.es.pycon.org/es/schedule/sysadmin-vs-django/">
  <img src="https://github.com/klashxx/PyConES2017/blob/01_auth/web/sysgate/static/img/logo_pycones17.png">
</a></h6>
<br>
<h6 align="center">Made with :heart: in Almería, Spain.</h6>


[license-svg]: https://img.shields.io/badge/license-MIT-blue.svg
[license-url]: https://opensource.org/licenses/MIT

[asciicast-01_auth-png]: https://asciinema.org/a/133210.png
[asciicast-01_auth-url]: https://asciinema.org/a/133210
