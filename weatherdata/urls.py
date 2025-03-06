from django.urls import path
from . import views


urlpatterns = [
    path('weather-data/', views.WeatherDataListCreateView.as_view(), name='weather-data-list'),
    path('weather-data/<int:pk>/', views.WeatherDataDetailView.as_view(), name='weather-data-detail'),
]