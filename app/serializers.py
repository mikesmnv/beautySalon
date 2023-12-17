from rest_framework import serializers
from .models import Services, Team


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['name', 'price', 'top_price', 'subcategorу', 'type']
        depth = 2
        read_only_fields = ['name', 'price', 'top_price', 'subcategorу', 'type']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'post', 'isTop', 'text', 'photo']
        read_only_fields = ['name', 'post', 'isTop', 'text', 'photo']