import uuid
from django.db import models
from django.utils import timezone


class UserModel(models.Model):
    id = models.CharField(max_length=100, primary_key=True)


class TodoModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, default=None)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=100, default=None)
    date = models.DateField(default=timezone.now)
    done = models.BooleanField(default=False)


class CharacterModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, default=None)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    level = models.PositiveSmallIntegerField(default=1)
    exp = models.PositiveIntegerField(default=0)
