from rest_framework import generics
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