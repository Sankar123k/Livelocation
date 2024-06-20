from rest_framework import generics
from .models import Location
from .serializers import LocationSerializer
from django.shortcuts import render

class LocationCreateView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all().order_by('-timestamp')[:1]  # Get the latest location
    serializer_class = LocationSerializer

    def location_map_view(request):
        return render(request, 'location_map.html')
    
   
        
