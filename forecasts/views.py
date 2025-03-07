from rest_framework import generics
from .models import Forecast
from .serializers import ForecastSerializer
from .pagination import ForecastPagination


class ForecastListCreateView(generics.ListCreateAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
    pagination_class = ForecastPagination

class ForecastDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer