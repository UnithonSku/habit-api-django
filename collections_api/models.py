import uuid
from django.db import models
from user_api.models import UserModel


class CharacterModel(models.Model):
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, default=None, related_name='characters')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    level = models.PositiveSmallIntegerField(default=1)
    exp = models.PositiveIntegerField(default=0)
