FROM python:3
MAINTAINER Juan Diego Godoy Robles
ENV PYTHONUNBUFFERED 1
RUN mkdir /sysgate /config
ADD ./requirements.txt /config/
RUN pip3 install --no-cache-dir -r /config/requirements.txt
RUN pip3 install --no-dependencies git+https://github.com/django-admin-bootstrapped/django-admin-bootstrapped.git
ADD . /sysgate/
WORKDIR /sysgate/
ENV PYTHONPATH /sysgate/sysgate

CMD ["gunicorn", "sysgate.wsgi", "--log-level=debug", "-w 2", "-b 0.0.0.0:8000"]
