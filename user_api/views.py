from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user_api.models import UserModel
from user_api.serializers import UserSerializer


class UserView(APIView):
    def post(self, request):
        print(request.data)
        print(request.POST)
        token = request.data['user']

        try:
            user_model = UserModel.objects.get(id=token)
            user_serializer = UserSerializer(instance=user_model)
            return Response(user_serializer.data)
        except UserModel.DoesNotExist:
            new_model = UserModel(id=token)
            new_model.save()
            user_serializer = UserSerializer(instance=new_model)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
