from rest_framework import serializers
from collections_api.models import CharacterModel


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterModel
        exclude = ('user', )
