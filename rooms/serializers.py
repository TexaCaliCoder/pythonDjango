from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    coordinates = serializers.CharField(required = False)
    id = serializers.IntegerField(primary_key=True)
    name = serializers.CharField(required = False)
    description = serializers.TextFieldrequired = False()
    class Meta:
        model = Room
        fields = ('coordinates', 'id', 'name', 'description', 'n', 's', 'e', 'w' )