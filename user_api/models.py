from django.db import models


class UserModel(models.Model):
    id = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return 'User: {}'.format(self.id)
