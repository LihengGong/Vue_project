from rest_framework import serializers
from . import models


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Note
        fields = ['id', 'author', 'title', 'content', 'create_time', 'last_modify_time']
