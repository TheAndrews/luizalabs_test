#!/bin/bash

python labs_test/manage.py makemigrations

python labs_test/manage.py migrate

python labs_test/manage.py collectstatic --noinput

python labs_test/manage.py createsuperuser

python labs_test/manage.py runserver 0.0.0.0:8000