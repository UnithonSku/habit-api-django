from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from collections_api.models import CharacterModel
from collections_api.serializers import CharacterSerializer


class CollectionsView(APIView):
    def post(self, request):
        pass


class CollectionsCreateView(APIView):
    def post(self, request):
        pass


class CollectionsUpdateView(APIView):
    def post(self, request):
        pass


class CollectionsDeleteView(APIView):
    def post(self, request):
        pass
