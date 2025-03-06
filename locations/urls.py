from django.urls import path
from . import views


urlpatterns = [
    path('locations/', views.LocationListCreateView.as_view(), name='locations-list'),
    path('locations/<int:pk>/', views.LocationDetailView.as_view(), name='location-detail'),
]