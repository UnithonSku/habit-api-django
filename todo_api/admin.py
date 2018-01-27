from django.contrib import admin
from user_api.models import UserModel
from todo_api.models import TodoModel
from collections_api.models import CharacterModel

admin.site.register(UserModel)
admin.site.register(TodoModel)
admin.site.register(CharacterModel)
