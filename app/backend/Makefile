SHELL=/bin/bash

collectstatic:
	python3 /app/manage.py collectstatic --no-post-process --noinput

migrate:
	python3 /app/manage.py migrate

runserver:
	python3 /app/manage.py runserver 0.0.0.0:8000

install:
	pip3 install -r /app/requirements.txt

dockerize:
	dockerize -wait tcp://db:5432 -timeout 20s

gunicorn:
	exec gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers=2 --threads=4

daphne:
	daphne -b 0.0.0.0 -p 8000 app.asgi:application