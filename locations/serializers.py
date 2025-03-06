from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'latitude', 'longitude', 'elevation', 'created_at']
        read_only_fields = ['id', 'created_at']

class LocationShortSerializer(serializers.ModelSerializer):
    model = Location
    fields = ['id', 'name']