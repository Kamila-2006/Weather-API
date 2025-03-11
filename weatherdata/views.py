from rest_framework import generics
from django.db.models import Avg, Sum, Max
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import WeatherData
from .serializers import WeatherDataSerializer
from .pagination import WeatherDataPagination


class WeatherDataListCreateView(generics.ListCreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    pagination_class = WeatherDataPagination

class WeatherDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

class LocationWeatherDataView(generics.ListAPIView):
    serializer_class = WeatherDataSerializer
    pagination_class = WeatherDataPagination

    def get_queryset(self):
        location_id = self.kwargs['location_id']
        return WeatherData.objects.filter(location_id=location_id)

class AverageTemperatureView(APIView):
    def get(self, request):
        avg_temp = WeatherData.objects.aggregate(average_temperature=Avg('temperature'))
        return Response(avg_temp)

class TotalPrecipitationView(APIView):
    def get(self, request):
        total_precip = WeatherData.objects.aggregate(total_precipitation=Sum('precipitation'))
        return Response(total_precip)

class MaxWindSpeedView(APIView):
    def get(self, request):
        max_wind_speed = WeatherData.objects.aggregate(max_wind_speed=Max('wind_speed'))
        return Response(max_wind_speed)