from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from . import models
from . import serializers


# Create your views here.
class ListNote(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['author']


class DetailNote(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
