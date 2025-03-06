from rest_framework import serializers
from .models import WeatherData


class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ['id', 'location', 'temperature', 'humidity', 'pressure', 'wind_speed', 'wind_direction', 'precipitation', 'recorded_at']
        read_only_fields = ['id', 'recorded_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['location'] = {
            'id': instance.location.id,
            'name': instance.location.name
        }
        return representation