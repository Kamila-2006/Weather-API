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

class ForecastsByLocation(generics.ListAPIView):
    serializer_class = ForecastSerializer
    pagination_class = ForecastPagination

    def get_queryset(self):
        location_id = self.kwargs['location_id']
        return Forecast.objects.filter(location_id=location_id)