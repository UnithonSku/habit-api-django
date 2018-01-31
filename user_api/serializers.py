from rest_framework import serializers
from user_api.models import UserModel
from todo_api.serializers import TodoSerializer
from collections_api.serializers import CharacterSerializer


class UserSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, required=False)
    characters = CharacterSerializer(many=True, required=False)

    class Meta:
        model = UserModel
        fields = ('id', 'todos', 'characters')


class UserTodoSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, required=True)

    class Meta:
        model = UserModel
        fields = ('id', 'todos')
