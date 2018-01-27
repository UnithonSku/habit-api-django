from rest_framework import serializers
from todo_api.models import UserModel, TodoModel, CharacterModel


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        exclude = ('user', )


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharacterModel
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)
    characters = CharacterSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = '__all__'
