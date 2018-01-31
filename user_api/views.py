from rest_framework import mixins, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from user_api.models import UserModel
from user_api.serializers import UserSerializer


class UserView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericAPIView):
    """
    View for users.
    Lists the detail of user if user does exist, creates user if does not
    """

    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            model = UserModel.objects.get(id=request.data['id'])
            serializer = self.get_serializer(model)
            return Response(serializer.data)
        except UserModel.DoesNotExist:
            return self.create(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data['id']
            if data == '':
                return Response({'error': 'user id must be provided'}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'error': 'user id must be provided'}, status=status.HTTP_400_BAD_REQUEST)

        return self.retrieve(request, *args, **kwargs)
