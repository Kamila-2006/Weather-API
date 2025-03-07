from django.urls import path
from . import views
from .views import ForecastDetailView, ForecastsByLocation

urlpatterns = [
    path('forecasts/', views.ForecastListCreateView.as_view(), name='forecast-list'),
    path('forecasts/<int:pk>/', ForecastDetailView.as_view(), name='forecast-detail'),
    path('forecasts/location/<int:location_id>/', ForecastsByLocation.as_view(), name='forecast-by-location'),
]