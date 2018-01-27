from django.urls import path
from collections_api.views import *

urlpatterns = [
    path('', CollectionsView.as_view()),
    path('create/', CollectionsCreateView.as_view()),
    path('update/', CollectionsUpdateView.as_view()),
    path('delete/', CollectionsDeleteView.as_view()),
]
