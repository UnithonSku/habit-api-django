from django.urls import path
from user_api.views import *

urlpatterns = [
    path('', UserView.as_view()),
]
