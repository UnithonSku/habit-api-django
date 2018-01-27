from django.urls import path
from todo_api.views import *

urlpatterns = [
    path('', TodoView.as_view()),
    path('create/', TodoCreateView.as_view()),
    path('update/', TodoUpdateView.as_view()),
    path('delete/', TodoDeleteView.as_view()),
]
