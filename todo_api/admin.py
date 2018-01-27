from django.contrib import admin
from todo_api.models import *

# Register your models here.
admin.site.register(UserModel)
admin.site.register(TodoModel)
admin.site.register(CharacterModel)
