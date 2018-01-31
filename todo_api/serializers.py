import datetime
from rest_framework import serializers
from todo_api.models import TodoModel


class DateSerializer(serializers.Serializer):
    year = serializers.IntegerField(min_value=0, allow_null=False)
    month = serializers.IntegerField(
        min_value=1, max_value=12, allow_null=False, default=1)
    day = serializers.IntegerField(
        min_value=1, max_value=30, allow_null=False, default=1)

    def create(self, validated_data):
        return None

    def update(self, instance, validated_data):
        return None


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = '__all__'


class TodoListRequestSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100, allow_blank=False)
    month = serializers.IntegerField(
        max_value=12, min_value=1, allow_null=False, default=1)

    def create(self, validated_data):
        return None

    def update(self, instance, validated_data):
        return None


class TodoCreateSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    start_date = serializers.DateField(default=datetime.date.today())
    end_date = serializers.DateField(default=datetime.date.today())
    order = serializers.IntegerField(max_value=5)

    def create(self, validated_data):
        return None

    def update(self, instance, validated_data):
        return None


class TodoCreateRequestSerializer(serializers.Serializer):
    user = serializers.CharField(
        max_length=100, allow_null=False, allow_blank=False)
    todo = serializers.CharField(
        max_length=100, allow_null=False, allow_blank=False)
    order = serializers.IntegerField(min_value=1, max_value=5, default=1)
    until = DateSerializer(many=False, required=True)

    def create(self, validated_data):
        return None

    def update(self, instance, validated_data):
        return None


class UpdateInfoSerializer(serializers.Serializer):
    title = serializers.CharField(
        max_length=100, allow_null=True, allow_blank=True, required=False)
    done = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return None

    def update(self, instance, validated_data):
        return None


class TodoUpdateRequestSerializer(serializers.Serializer):
    user = serializers.CharField(
        max_length=100, allow_null=False, allow_blank=False)
    todo = serializers.CharField(
        max_length=100, allow_null=False, allow_blank=False)
    update = UpdateInfoSerializer(required=True, many=False)

    def create(self, validated_data):
        return None
