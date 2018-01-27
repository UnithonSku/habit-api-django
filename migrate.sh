#!/usr/bin/env bash
python manage.py makemigrations user_api
python manage.py makemigrations collections_api
python manage.py makemigrations todo_api
python manage.py migrate