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
