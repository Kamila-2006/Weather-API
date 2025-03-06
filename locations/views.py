from rest_framework import generics
from .models import Location
from .serializers import LocationSerializer
from .pagination import LocationListPagination


class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    pagination_class = LocationListPagination

class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer