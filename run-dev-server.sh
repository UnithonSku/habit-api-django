#!/usr/bin/env bash
python manage.py makemigrations user_api --settings=habit_api_django.settings.dev
python manage.py makemigrations collections_api --settings=habit_api_django.settings.dev
python manage.py makemigrations todo_api --settings=habit_api_django.settings.dev
python manage.py migrate --settings=habit_api_django.settings.dev
python manage.py runserver --settings=habit_api_django.settings.dev --verbosity=3
