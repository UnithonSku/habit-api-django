from rest_framework import serializers
from todo_api.models import TodoModel


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        exclude = ('user', )
