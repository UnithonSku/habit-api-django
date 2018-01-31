from habit_api_django.settings.base import *

DEBUG = True

ALLOWED_HOSTS = [
    'habitapidjango-env.ap-northeast-2.elasticbeanstalk.com',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['HABIT_API_DATABASE'],
        'USER': os.environ['HABIT_API_USER'],
        'PASSWORD': os.environ['HABIT_API_PASSWORD'],
        'HOST': os.environ['HABIT_API_HOST'],
        'PORT': '3306',
    }
}
