install:
	poetry install

dev:
	poetry run python manage.py runserver

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) hockey_django_project.wsgi

lint:
	poetry run flake8 hockey_django_project

test:
	poetry run python3 manage.py test

test-coverage:
	poetry run coverage run --source='.' manage.py test hockey_django_project
	poetry run coverage xml
	poetry run coverage report


check:
	poetry check

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

locale_up:
	django-admin makemessages -l ru

locale_com:
	django-admin compilemessages

.PHONY: install dev start lint build test test-coverage check migrate locale_up locale_com