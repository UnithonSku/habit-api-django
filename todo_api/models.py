import datetime
import uuid
from django.db import models
from django.forms import ValidationError
from user_api.models import UserModel


class TodoModel(models.Model):
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, default=None)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=100, default=None)
    date = models.DateField(default=datetime.date.today())
    done = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return 'Todo {} by User {}'.format(self.title, self.user)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.order < 1 or self.order > 5:
            raise ValidationError('Order must be between 1 and 5')
        super(TodoModel, self).save()
