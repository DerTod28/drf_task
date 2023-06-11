THIS_FILE := $(lastword $(MAKEFILE_LIST))
.PHONY: help build up start down destroy stop restart logs logs-api ps login-timescale login-api db-shell
help:
		make -pRrq  -f $(THIS_FILE) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'
build:
		docker-compose -f docker-compose.yml --env-file deploy/docker/.env up --build$(c)
down:
		docker-compose -f docker-compose.yml down $(c)
destroy:
		docker-compose -f docker-compose.yml down --rmi all --volumes $(c)
stop:
		docker-compose -f docker-compose.yml stop $(c)
restart:
		docker-compose -f docker-compose.yml stop $(c)
		docker-compose -f docker-compose.yml up -d $(c)
db-shell:
		docker exec -it drf_task-db-1 bash
createsuperuser:
		docker exec drf_task-django-1 python manage.py createsuperuser --no-input
migrate:
		docker exec drf_task-django-1 python manage.py makemigrations
		docker exec drf_task-django-1 python manage.py migrate
collectstatic:
		docker exec drf_task-django-1 python manage.py collectstatic --noinput
tests:
		docker exec drf_task-django-1 python manage.py test