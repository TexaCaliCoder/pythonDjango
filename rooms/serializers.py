from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    coordinates = serializers.CharField(required = False)
    id = models.IntegerField(required = False)
    name = serializers.CharField(required = False)
    description = serializers.CharField(required = False)
    class Meta:
        model = Room
        fields = ('coordinates', 'id', 'name', 'description', 'n', 's', 'e', 'w' )