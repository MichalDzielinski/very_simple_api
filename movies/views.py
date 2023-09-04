from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MoviedataSerializer
from .models import Moviedata


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class  = MoviedataSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='action')
    serializer_class = MoviedataSerializer