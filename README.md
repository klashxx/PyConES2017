# :snake: Sysadmin vs Django
[![][license-svg]][license-url]

*Demo* que ilustrará la charla [*Sysadmin vs Django*](https://2017.es.pycon.org/es/schedule/sysadmin-vs-django/) en la [PyConES Cáceres 2017](http://2017.es.pycon.org/).

Basado en el [post][blog-post] del mismo nombre.

## Pruébalo en tu equipo

Todo el software se ha *dockerizado* de forma que la aplicación pueda levantarse independientemente del entorno del usuario.

El repositorio se estructura en [*ramas*](https://git-scm.com/docs/git-branch), usándose cada una de ellas para ilustrar un tema en concreto.

Requisitos:

- Cliente [git][git-download].

- [Docker][docker-install] y [Docker Compose][docker-compose-install].

La dinámica de instalación es siempre muy similar:

- `checkout` de la rama.

- Ejecución de comandos en `docker-compose`.

Las instrucciones detalladas se pueden encontrar en los `README.md` de las *branches* y en los vídeos *linkados* (¡gracias [asciinema][asciinema]!).

Cada una de las ramas es _usable per se_ y demuestran cómo implementar una funcionalidad concreta, además son **incrementales**, es decir, las modificaciones realizadas en una `branch` son *reusadas* en la siguiente.

## :point_right: ¡Listo! ¡Vamos con primer [*paso*][repo-auth]! :point_left:

<br>

### :warning: Para los impacientes :warning:

Aunque la **experiencia ideal de aprendizaje la proporciona la instalación por fases**, también es posible la instalación *en un paso* siguiendo estas instrucciones:

```
$ git clone https://github.com/klashxx/PyConES2017.git sysgate
$ cd sysgate/
$ docker-compose up -d
$ docker-compose exec sysgate python manage.py migrate
$ docker-compose exec sysgate python manage.py createsuperuser
$ docker-compose exec sysgate python manage.py loaddata sysgate/fixtures/auth.group.json
$ docker-compose exec sysgate python manage.py loaddata sysgate/fixtures/account.user.json
$ docker-compose exec sysgate python manage.py loaddata sysgate/fixtures/metrics.metrica.json
$ docker-compose exec sysgate python manage.py collectstatic --noinput
```

[![Sysgate][asciicast-master-png]][asciicast-master-url]

Abre tu navegador apuntando al [localhost][localhost] y prueba la aplicación.

:warning: **ATENCION**: Es posible que tengas que purgar la `BD` si antes optaste por la instalacion en fases: `rm -rf ~/data/postgresql`

## Contacta conmigo

Mis perfiles online están [**aquí**](https://klashxx.github.io/about), no te cortes ... :godmode:

<h6 align="center">
<a href="https://2017.es.pycon.org/es/schedule/sysadmin-vs-django/">
  <img src="https://github.com/klashxx/PyConES2017/blob/master/web/sysgate/static/img/logo_pycones17.png">
</a></h6>
<br>
<h6 align="center">Made with :heart: in Almería, Spain.</h6>

[pycones2017-home]: https://2017.es.pycon.org "PyConES 2017 - Cáceres"
[dvs-agenda]: https://2017.es.pycon.org/es/schedule/sysadmin-vs-django/ "Django vs Sysadmin - PyConES 2017"
[blog-post]: https://klashxx.github.io/django-vs-sysadmin "Django vs Sysadmin Blog Post"
[dvs-slides]: https://klashxx.github.io/slides/django/ "Django vs Sysadmin - Slides"
[github]: https://github.com "GitHub"
[asciinema]: https://asciinema.org/ "asciinema"
[git-download]: https://git-scm.com/downloads "git - Descarga"
[docker-install]: https://docs.docker.com/engine/installation/ "Docker - Instalación"
[docker-compose-install]: https://docs.docker.com/compose/install/ "Docker Compose - Instalación"
[git-branch]: https://git-scm.com/book/es/v1/Ramificaciones-en-Git-%C2%BFQu%C3%A9-es-una-rama%3F "¿Qué es una rama?"
[repo-auth]: https://github.com/klashxx/PyConES2017/tree/01_auth "Django vs Sysadmin - 01_auth"
[localhost]: http://0.0.0.0/
[asciicast-master-png]: https://asciinema.org/a/137226.png
[asciicast-master-url]: https://asciinema.org/a/137226
[license-svg]: https://img.shields.io/badge/license-MIT-blue.svg
[license-url]: https://opensource.org/licenses/MIT
