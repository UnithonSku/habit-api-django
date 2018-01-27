import datetime
import uuid
from django.db import models
from user_api.models import UserModel


class TodoModel(models.Model):
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, default=None, related_name='todos')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=100, default=None)
    date = models.DateField(default=datetime.date.today())
    done = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=1)
