from habit_api_django.settings.base import *

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'settings/db.sqlite3'),
    }
}
