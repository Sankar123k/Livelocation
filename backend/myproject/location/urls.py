from django.urls import path
from .views import LocationCreateView, LocationListView

urlpatterns = [
    path('api/location/', LocationCreateView.as_view(), name='location-create'),
    path('api/latest-location/', LocationListView.as_view(), name='location-list'),
]
