from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ServicesSerializer, TeamSerializer
from .models import Services, Team


class ServicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Services.objects.all().select_related('subcategorу')
    serializer_class = ServicesSerializer


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

# Create your views here.
